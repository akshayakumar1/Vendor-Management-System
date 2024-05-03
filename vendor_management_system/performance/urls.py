from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/<int:vendor_id>/performance/', views.VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]
