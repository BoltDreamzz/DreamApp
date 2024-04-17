from django.contrib import admin
from django.conf import settings

from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shop.urls")),
    path('user/', include("userauths.urls")),
    path('cart/', include("cart.urls")),
    path('search/', include("search.urls")),
    path('wishlist/', include("wishlist.urls")),
    path("", include("pwa.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
