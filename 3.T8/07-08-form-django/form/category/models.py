from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=20,verbose_name='Mã') # Sử dụng verbose_name để đặt tên tiếng Việt cho trường
    name = models.CharField(max_length=100,verbose_name='Tên')
    def __str__(self):
        return self.name

