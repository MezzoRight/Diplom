from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    logo = models.ImageField(upload_to='brands_logos/', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    logo = models.ImageField(upload_to='shops_logos/', verbose_name='Логотип')
    link = models.URLField(verbose_name='Сайт')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главные категории'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    category = models.ForeignKey(Category, related_name='subcategories',
                                 on_delete=models.CASCADE, verbose_name='Выберите категорию')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    model = models.CharField(max_length=64, verbose_name='Модель')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, verbose_name='Бренд')
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products_images/', verbose_name='Фото') # TODO: сделать картинку по умолчанию

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографиии'

    def __str__(self):
        return self.product.name

class ProductsShop(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    shop = models.ForeignKey(Shop, related_name='products_shop', 
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products_shop', 
                                on_delete=models.CASCADE)
    link = models.URLField(verbose_name='Ссылка на товар')

    subcategory = models.ForeignKey(SubCategory, related_name='products_shop', on_delete=models.CASCADE, verbose_name='Выберите категорию')

    class Meta:
        verbose_name = 'Продукты в магазине'
        verbose_name_plural = 'Продукты в магазинах'

    def __str__(self):
        return f'{self.product.name} ({self.shop.name})'

class ProductAttribute(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='attributes'
    )

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f'{self.product} - {self.name}'