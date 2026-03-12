from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # Login
    path('login/', views.UserLoginView.as_view(), name='login'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Product URLs
    path('product_list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    # Service URLs
    path('service-requests/', views.service_request_list, name='service_request_list'),
    path('service-requests/add/', views.add_service_request, name='add_service_request'),
    path('service-requests/update/<int:id>/', views.update_service_request, name='update_service_request'),
    path('service-requests/delete/<int:id>/', views.delete_service_request, name='delete_service_request'),

    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),
]