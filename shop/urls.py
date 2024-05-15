from django.urls import path
from . import views
from django.urls import path

# from your_app.views import custom_404

app_name = "shop"

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('customize/', views.customize, name='customize'),

    path('product-partials/', views.products_partial, name='products_partial'),

    path('contact/', views.contact_page, name='contact'),

    path('splash/', views.splash, name='splash'),
    path('orders/', views.order_page, name='order_page'),
    path('order-success/', views.order_success, name='order_success'),

    path('categories/', views.category_page, name='categories'),
    path('detail-order/', views.order_detail, name='order_detail'),

    path('detail/<int:pk>/', views.detail, name='detail'),
    # path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),

    path('products-by-category/<int:category_id>/', views.products_by_category, name='products_by_category'),

    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
