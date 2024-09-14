from django.contrib import admin
from .models import BookPurchase, Purchase

@admin.register(BookPurchase)
class BookPurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'title', 'quantity', 'list_price')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_purchase')
    
