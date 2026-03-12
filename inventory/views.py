from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.timezone import now

from .models import Product, ServiceRequest
from .forms import ProductForm, ServiceRequestForm


class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return '/dashboard/'

        #   DASHBOARD


@login_required
def dashboard(request):
    completed_services = ServiceRequest.objects.filter(service_status='Completed')

    total_revenue = sum(service.product.selling_price for service in completed_services)
    total_profit = sum(service.product.profit for service in completed_services)

    total_services = ServiceRequest.objects.count()
    pending_services = ServiceRequest.objects.filter(service_status='Pending').count()
    completed_count = completed_services.count()

    total_products = Product.objects.count()
    low_stock = Product.objects.filter(stock_quantity__lte=2)

    context = {
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'total_services': total_services,
        'pending_services': pending_services,
        'completed_count': completed_count,
        'total_products': total_products,
        'low_stock': low_stock,
    }

    return render(request, 'dashboard.html', context)

    # PRODUCT VIEWS


@login_required
@permission_required('inventory.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


@login_required
@permission_required('inventory.add_product', raise_exception=True)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'inventory/product_form.html', {'form': form})


@login_required
@permission_required('inventory.change_product', raise_exception=True)
def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/product_form.html', {'form': form})


@login_required
@permission_required('inventory.delete_product', raise_exception=True)
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')

    # SERVICE REQUEST VIEWS


@login_required
@permission_required('inventory.view_servicerequest', raise_exception=True)
def service_request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'inventory/service_request_list.html', {'requests': requests})


@login_required
@permission_required('inventory.add_servicerequest', raise_exception=True)
def add_service_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            product = service.product

            if product.stock_quantity <= 0:
                form.add_error('product', 'This product is out of stock.')
            else:
                with transaction.atomic():
                    product.stock_quantity -= 1
                    product.save()
                    service.save()
                return redirect('service_request_list')

    else:
        form = ServiceRequestForm()

    return render(request, 'inventory/service_request_form.html', {'form': form})


@login_required
@permission_required('inventory.change_servicerequest', raise_exception=True)
def update_service_request(request, id):
    service = get_object_or_404(ServiceRequest, id=id)
    old_status = service.service_status

    if request.method == "POST":
        form = ServiceRequestForm(request.POST, instance=service)

        if form.is_valid():
            updated = form.save(commit=False)

            if updated.service_status == "Completed" and old_status != "Completed":
                updated.returned_date = now().date()

            updated.save()
            return redirect('service_request_list')

    else:
        form = ServiceRequestForm(instance=service)

    return render(request, 'inventory/service_request_form.html', {'form': form})


@login_required
@permission_required('inventory.delete_servicerequest', raise_exception=True)
def delete_service_request(request, id):
    service = get_object_or_404(ServiceRequest, id=id)
    service.delete()
    return redirect('service_request_list')

