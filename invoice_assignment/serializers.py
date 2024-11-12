from rest_framework import serializers
from .models import *


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        exclude = ['id', 'invoice']


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        invoice_details = validated_data.pop('details', [])
        invoice = Invoice.objects.create(**validated_data)
        for invoice_detail in invoice_details:
            InvoiceDetail.objects.create(invoice=invoice, **invoice_detail)
        return invoice

    def update(self, instance, validated_data):
        invoice_details = validated_data.pop('details', [])
        instance.customer_name = validated_data.get(
            'customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        instance.details.all().delete()
        for invoice_detail in invoice_details:
            InvoiceDetail.objects.create(invoice=instance, **invoice_detail)
        return instance
