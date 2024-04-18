from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WishlistItem


@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    wish_count = wishlist_items.count()
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items, 'wish_count': wish_count,})


@login_required
def add_to_wishlist(request, product_id):
    if WishlistItem.objects.filter(user=request.user, product_id=product_id).exists():
        messages.info(request, "Sorry the product already exists in your wishlist")
        # Item already in wishlist
        return redirect('wishlist:wishlist')
    else:
        WishlistItem.objects.create(user=request.user, product_id=product_id)
        messages.info(request, "Product has been added to wishlist")

        return redirect('shop:detail', product_id)


@login_required
def remove_from_wishlist(request, product_id):
    WishlistItem.objects.filter(user=request.user, product_id=product_id).delete()
    messages.info(request, "Product removed from wishlist")

    return redirect('shop:detail', product_id)
