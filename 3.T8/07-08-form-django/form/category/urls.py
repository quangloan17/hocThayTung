from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('list_category', listCategory,name='list-category'),    
    path('create_category', createCategory,name='create-category'),    
    path('update_category/<pk>', updateCategory,name='update-category'),
    path('delete_category/<pk>', deleteCategory,name='delete-category'),
]
