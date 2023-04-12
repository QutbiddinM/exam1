from django import forms
from .models import Blog, BlogCategory, Product, ProductCategory
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        BlogCategory.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('created_at',)


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        ProductCategory.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('created_at',)