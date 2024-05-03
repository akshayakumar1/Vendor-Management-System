from rest_framework import serializers
from .models import PurchaseOrder
from vendors.serializers import VendorSerializer


class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

