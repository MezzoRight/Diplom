from django.contrib import admin
from django.urls import path

from .views import home_view, brands_view, shops_view, products_view, product_search, product_detail, products_by_shop

urlpatterns = [
    path('', home_view, name='home'),
    path('brands/', brands_view, name='brands'),
    path('shops/', shops_view, name='shops'),
    path('shops/<int:shop_id>/', products_by_shop, name='products_by_shop'),
    path('products/<int:subcategory_id>/', products_view, name='products'),
    path('products/search/', product_search, name='product_search'),
    path('products/detail/<int:product_id>/', product_detail, name='product_detail'),
]