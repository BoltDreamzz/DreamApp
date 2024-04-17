from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
from userauths.models import User
from shop.models import Product


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'product'], name='unique_wishlist_item')
        ]
