from django.urls import path
from .views import ProductListCreate, product_page

urlpatterns = [
    path('', product_page, name='product-page'),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
   ]