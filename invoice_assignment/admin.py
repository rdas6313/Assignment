from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    pass
