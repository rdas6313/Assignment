from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get', 'post', 'put', 'head', 'option']
    lookup_field = 'invoice_number'

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')
