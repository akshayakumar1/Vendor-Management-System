from django.urls import path
from vendors import views
urlpatterns = [
    path('api/vendors/', views.VendorListAPIView.as_view(), name='vendor-list'),

    path('api/vendors/<int:vendor_id>/', views.VendorDetailAPIView.as_view(), name='vendor-detail'),

    
]