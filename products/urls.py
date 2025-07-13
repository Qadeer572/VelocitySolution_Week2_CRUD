from django.contrib import admin
from django.urls import path
from django.urls import include
from products.views import productsList,addProduct,updateProduct
urlpatterns = [

    path('getProducts/', productsList.as_view(), name='products-list'),
    path('addProduct/', addProduct.as_view(), name='add-product'),
    path('updateProduct/', updateProduct.as_view(), name='update-product'),
    
]