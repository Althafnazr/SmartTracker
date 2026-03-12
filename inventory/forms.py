from django import forms

from .models import Product
from .models import ServiceRequest


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_stock_quantity(self):
        stock = self.cleaned_data.get('stock_quantity')
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
