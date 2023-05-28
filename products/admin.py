from django.contrib import admin

from .models import Product, ProductAttribute, Category, SubCategory, Brand, ProductsShop, Shop, ProductImage


admin.site.register((Product, ProductAttribute, Category, SubCategory, Brand, ProductsShop, Shop, ProductImage))