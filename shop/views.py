from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from cart.models import Order
from wishlist.models import WishlistItem


def splash(request):
    return render(request, "shop/splash.html")


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    kiddiesCat = Category.objects.get(name="Kiddies")
    BarbiesCat = Category.objects.get(name="Women")
    kiddiesPro = kiddiesCat.product_set.all()
    BarbiesPro = BarbiesCat.product_set.all()

    products_by_category = {}
    for category in categories:
        products_by_category[category] = Product.objects.filter(category=category)[:2]

    # productCat = products.filter(categories=categories)

    return render(request, "shop/index.html", {
        "categories": categories,
        "products": products,
        "products_by_category": products_by_category,
        "kiddiesPro": kiddiesPro,
        "BarbiesPro": BarbiesPro,
    })


# @login_required
def explore(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "shop/explore.html", {
        "categories": categories,
        "products": products,
    })


@login_required
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_sold=False)
    related_items = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)

    # Check if the product is in the user's wishlist
    product_in_wishlist = WishlistItem.objects.filter(user=request.user, product=product).exists()

    return render(request, "shop/detail.html", {
        "related_items": related_items,
        "product": product,
        "product_in_wishlist": product_in_wishlist,
    })


# @login_required
# def detail(request, pk):
#     product = get_object_or_404(Product, pk=pk, is_sold=False)
#     related_items = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)
#
#     return render(request, "shop/detail.html", {
#         "related_items": related_items,
#         "product": product,
#     })


@login_required
def category_page(request):
    categories = Category.objects.all()
    category_count = categories.count()

    return render(request, "shop/category_page.html", {
        "categories": categories,
        "category_count": category_count,
    })


@login_required
def products_by_category(request, category_id):
    # Retrieve the category object based on the category_id
    category = Category.objects.get(pk=category_id)

    # Filter products based on the selected category
    products = Product.objects.filter(category=category)
    products_count = products.count()

    context = {
        'category': category,
        'products': products,
        'products_count': products_count,
    }

    return render(request, 'shop/explore.html', context)


@login_required
def order_page(request):
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count()

    return render(request, "shop/order_page.html", {
        "orders": orders,
        "order_count": order_count,
    })


@login_required
def order_detail(request):
    # order = get_object_or_404(Order, pk=order_id, user=request.user)

    return render(request, "shop/order_detail.html", {
        # "order": order,
    })


def order_success(request):
    # order = get_object_or_404(Order, pk=order_id, user=request.user)

    return render(request, "shop/order_success.html", {
        # "order": order,
    })
