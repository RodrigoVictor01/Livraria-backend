from django.db import models
from users.models import User
import uuid

class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_purchase(self):
        return sum(book.list_price * book.quantity for book in self.book_purchases.all())

    def __str__(self):
        return f"Compra {self.id} - Total: {self.total_purchase:.2f}"

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


class BookPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='book_purchases', on_delete=models.CASCADE)
    book_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    authors = models.JSONField() 
    list_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Book Purchase'
        verbose_name_plural = 'Book Purchases'


