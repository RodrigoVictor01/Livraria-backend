from rest_framework import serializers
from .models import Purchase, BookPurchase
from users.models import User

class BookPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPurchase
        fields = ['book_id', 'title', 'quantity', 'authors', 'list_price']

class PurchaseSerializer(serializers.ModelSerializer):
    book_purchases = BookPurchaseSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Purchase
        fields = ['user', 'total_purchase', 'created_at', 'book_purchases']

    def create(self, validated_data):
        book_purchases_data = validated_data.pop('book_purchases')
        user = validated_data.pop('user')
        purchase = Purchase.objects.create(user=user, **validated_data)
        
        for book_data in book_purchases_data:
            BookPurchase.objects.create(purchase=purchase, **book_data)
        
        return purchase
