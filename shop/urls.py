from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('splash/', views.splash, name='splash'),

    path('categories/', views.category_page, name='categories'),

    path('detail/<int:pk>/', views.detail, name='detail'),
    path('products-by-category/<int:category_id>/', views.products_by_category, name='products_by_category'),

    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
