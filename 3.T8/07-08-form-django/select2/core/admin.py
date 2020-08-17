from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Entry)
admin.site.register(Language)
admin.site.register(Khachhang)
admin.site.register(Donhang)
admin.site.register(Donhangct)
