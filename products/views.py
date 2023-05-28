from django.shortcuts import render, get_object_or_404

from .models import Product, ProductsShop, Brand, Shop, Category, SubCategory, ProductAttribute, ProductImage
from .forms import ProductSearchForm


def home_view(request):
    productShops = ProductsShop.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    form = ProductSearchForm(request.GET)

    context = {'products_shop': productShops, 
               'subcategories': subcategories,
               'categories': categories,
               'form': form}
    return render(request, 'old/index.html', context)

def brands_view(request):
    brands = Brand.objects.all()
    all_brands = []
    form = ProductSearchForm(request.GET)
    categories = Category.objects.all()

    for brand in brands:
        brand_info = {
            'name': brand.name,
            'logo': brand.logo,
        }
        all_brands.append(brand_info)
    context = {'all_info': all_brands, 'form': form,
               'categories': categories}

    return render(request, 'old/brands.html', context)

def shops_view(request):
    shops = Shop.objects.all()
    form = ProductSearchForm(request.GET)
    categories = Category.objects.all()
    all_shops = []

    for shop in shops:
        shop_info = {
            'id': shop.id,
            'name': shop.name,
            'logo': shop.logo,
        }
        all_shops.append(shop_info)
    context = {'all_info': all_shops, 'form': form,
                'categories': categories}

    return render(request, 'old/shops.html', context)

def products_view(request, subcategory_id):
    form = ProductSearchForm(request.GET)
    subcategory = SubCategory.objects.get(id=subcategory_id)
    products = ProductsShop.objects.filter(subcategory=subcategory)
    categories = Category.objects.all()
    return render(request, 'old/products.html', {'subcategory': subcategory, 'products_shop': products,
                                             'categories': categories, 'form': form})

def product_search(request):
    form = ProductSearchForm(request.GET)
    productsShop = []
    search_query = ''

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        # Выполнение поиска продуктов без учета регистра символов
        productsShop = ProductsShop.objects.filter(product__name__icontains=search_query)

    categories = Category.objects.all()
    context = {
        'form': form,
        'products_shop': productsShop,
        'categories': categories,
        'search_query': search_query  # Передача значения запроса на поиск в контекст
    }

    return render(request, 'old/product_search.html', context)

def product_detail(request, product_id):
    product_shop = get_object_or_404(ProductsShop, id=product_id)
    categories = Category.objects.all()
    attributes = ProductAttribute.objects.filter(product=product_shop.product)
    products = ProductsShop.objects.filter(subcategory=product_shop.subcategory)
    images = ProductImage.objects.filter(product=product_shop.product)
    form = ProductSearchForm(request.GET)
    shops = ProductsShop.objects.filter(product=product_shop.product)
    print(shops)
    context = {
        'product_shop': product_shop,
        'categories': categories,
        'form': form,
        'attributes': attributes,
        'product_shop_name': product_shop.shop.name,
        'products_shop': products,
        'images': images,
        'shops': shops,
    }
    return render(request, 'old/product-details.html', context)


def products_by_shop(request, shop_id):
    products = ProductsShop.objects.filter(shop_id=shop_id)
    shop = Shop.objects.get(id=shop_id)
    categories = Category.objects.all()
    form = ProductSearchForm(request.GET)

    return render(request, 'old/shops_products.html', context= {'products': products,
                                                       'categories': categories,
                                                       'form': form,
                                                       'shop_name': shop.name})
