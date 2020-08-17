from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    code = models.CharField(max_length=20,verbose_name='Mã') # Sử dụng verbose_name để đặt tên tiếng Việt cho trường
    name = models.CharField(max_length=100,verbose_name='Tên')
    price = models.FloatField(verbose_name='Giá')
    image = models.ImageField(upload_to='static/images'
                                ,blank=True,verbose_name='Ảnh')

    def __str__(self):
        return self.name
    