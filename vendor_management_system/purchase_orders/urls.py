from django.urls import path
from . import views

urlpatterns = [
    path('api/purchase_orders/', views.PurchaseOrderListAPIView.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:po_id>/', views.PurchaseOrderDetailAPIView.as_view(), name='purchase-order-detail'),
    
    path('api/purchase_orders/<int:po_id>/acknowledge/', views.AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge-purchase-order'),

]
