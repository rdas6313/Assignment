from .views import *
from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')

urlpatterns = router.urls
