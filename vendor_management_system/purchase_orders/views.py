from django.shortcuts import render

from django.utils import timezone
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.





class PurchaseOrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, po_id):
        try:
            return PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            # print("my get_object() except call.................")
            raise NotFound()

    def get(self, request, po_id, format=None):
        purchase_order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_id, format=None):
        purchase_order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id, format=None):
        purchase_order = self.get_object(po_id)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AcknowledgePurchaseOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, po_id, format=None):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            print(purchase_order, "...") # #142 ...
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update acknowledgment date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        return Response({"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)

