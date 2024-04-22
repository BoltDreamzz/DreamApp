from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order, OrderItem
from .forms import OrderForm
from userauths.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Product, Category


@login_required
def shopping_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    cart_item_count = cart_items.count()
    total_price = user_cart.calculate_total_price()
    return render(request, 'cart/shopping_cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_item_count': cart_item_count,
    })


def cart_total(products):
    return sum(product.price for product in products)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to cart")

    return redirect('cart:shopping_cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)

    # Get the first instance of the specified product in the cart
    cart_item = user_cart.cartitem_set.filter(product=product).first()

    # Check if the cart item exists before attempting to decrement the quantity
    if cart_item:
        if cart_item.quantity > 1:
            # Decrement the quantity by 1
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Cart updated")
        else:
            # If the quantity is 1, remove the entire cart item
            cart_item.delete()
            messages.success(request, "Cart cleared")

    return redirect('cart:shopping_cart')


# Create your views here.
@login_required
def placeOrder(request):
    try:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                cart = get_object_or_404(Cart, user=request.user)

                order = Order.objects.create(
                    user=request.user,
                    status='Pending',
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    shipping_address=form.cleaned_data['shipping_address']
                )

                for cart_item in cart.cartitem_set.all():
                    OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
                cart.cartitem_set.all().delete()

                messages.success(request, "Congratulations, your order has been placed!")
                user_email = request.user.email

                # Prepare email content
                subject = 'Order Confirmation'
                html_message = render_to_string('shop/order_success.html', {'order': order})
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to_email = [user_email]

                send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

                return redirect('shop:order_success')
    except Exception as e:
        # Handle the error here
        error_message = str(e)
        return render(request, "shop/order_success.html", {'error_message': error_message})

    else:
        form = OrderForm()

    return render(request, "cart/checkout.html", {'form': form})

# def placeOrder(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             cart = get_object_or_404(Cart, user=request.user)
#
#             order = Order.objects.create(
#                 user=request.user,
#                 status='Pending',
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 phone_number=form.cleaned_data['phone_number'],
#                 shipping_address=form.cleaned_data['shipping_address']
#             )
#
#             for cart_item in cart.cartitem_set.all():
#                 OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
#             cart.cartitem_set.all().delete()
#
#             messages.success(request, "Congratulations, your order has been placed!")
#             user_email = request.user.email
#
#             # Prepare email content
#             subject = 'Order Confirmation'
#             html_message = render_to_string('shop/order_success.html', {'order': order})
#             plain_message = strip_tags(html_message)
#             from_email = settings.EMAIL_HOST_USER
#             to_email = [user_email]
#
#             send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
#
#             return redirect('shop:order_success')
#     else:
#         form = OrderForm()
#
#     return render(request, "cart/checkout.html", {'form': form})
