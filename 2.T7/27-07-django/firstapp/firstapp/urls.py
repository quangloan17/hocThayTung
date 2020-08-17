from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('hello',hello),
    path('tim_kiem/<ten>/<tuoi>',search),
]
