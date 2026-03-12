from django.db import models
from django.core.exceptions import ValidationError



class Product(models.Model):
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    part_name=models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    warranty_months = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def clean(self):
        if self.stock_quantity is not None and self.stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative.")

    def __str__(self):
        return f"{self.brand} {self.model_name} — {self.part_name}"

    @property
    def profit(self):
        return self.selling_price - self.purchase_price

    @property
    def total_profit(self):
        return self.profit * self.stock_quantity


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    issue_description = models.TextField()
    service_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    received_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product}"
