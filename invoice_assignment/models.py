from django.db import models
from .validators import *
from django.core.validators import MinValueValidator


class Invoice(models.Model):
    """
    This model represents a invoice.
    """
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=255, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"invoice no: {self.invoice_number} , customer name: {self.customer_name}"


class InvoiceDetail(models.Model):
    """
    This model represent details of an invoice
    """
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[validate_price])
    line_total = models.DecimalField(
        max_digits=15, decimal_places=2, validators=[validate_price])

    def __str__(self):
        return f"invoice: {self.invoice}, quantity: {self.quantity}, price: {self.price}, total: {self.line_total}"
