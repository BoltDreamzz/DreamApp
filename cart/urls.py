# urls.py
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    # path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('place-order/', views.placeOrder, name='place_order'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),

    # Add similar URLs for signup, logout, etc.
]
