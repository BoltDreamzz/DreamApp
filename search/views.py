from django.shortcuts import render

from django.db.models import Q

from shop.models import Product, Category


def find(request):
    query = request.GET.get("query", "")
    items = Product.objects.filter(is_sold=False)
    items_count = items.count()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
        items_count = items.count()

    return render(request, "search/find.html", {
        "items": items,
        "query": query,
        "items_count": items_count,
    })
