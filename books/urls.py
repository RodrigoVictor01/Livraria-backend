from django.urls import path
from .views import PurchaseCreateView

urlpatterns = [
    path('purchase/', PurchaseCreateView.as_view(), name='purchase-create'),
]
