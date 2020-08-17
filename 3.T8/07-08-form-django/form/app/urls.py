from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index,name='index'),    
    path('list_product', listProduct,name='list-product'),    
    path('create_product', createProduct,name='create-product'),    
    path('update_product/<pk>', updateProduct,name='update-product'),
    path('delete_product/<pk>', deleteProduct,name='delete-product'),

]
