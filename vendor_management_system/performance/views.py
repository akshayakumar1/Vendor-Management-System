from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

class VendorPerformanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id, format=None):
        print("VendorPerformanceAPIView called...")
        performances = HistoricalPerformance.objects.filter(vendor=vendor_id)
        serializer = HistoricalPerformanceSerializer(performances, many=True)
        return Response(serializer.data)

