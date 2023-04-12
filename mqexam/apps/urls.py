from django.urls import path
from .views import blogs, add_blog, one_blog, add_comment_blog, products_page, one_product,add_comment_product

urlpatterns = [
    path('', blogs, name='blogs'),
    path('add_blog', add_blog, name='add_blog'),
    path('blog/<int:pk>', one_blog, name='one_blog'),
    path('add_comment_blog/<int:pk>', add_comment_blog, name='add_comment_blog'),
]

products = [
    path('products/', products_page, name='products'),
    path('product/<int:pk>', one_product, name='one_product'),
    path('add_comment_product/<int:pk>', add_comment_product,
         name='add_comment_product'),

]

urlpatterns += products