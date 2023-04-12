from django.contrib import admin
from .models import BlogCategory, Blog, Product, ProductCategory


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)