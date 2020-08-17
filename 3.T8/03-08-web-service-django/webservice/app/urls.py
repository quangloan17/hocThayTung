from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('hello', hello),
    path('search_product', searchProduct),
]

# Lưu ý khi đặt tên cho đường dẫn thì đi với dấu gạch dưới,
#  còn tên hàm định nghĩa bằng camelcase (Chữ viết hoa từ chữ thứ 2)