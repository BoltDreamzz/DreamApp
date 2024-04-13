from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
