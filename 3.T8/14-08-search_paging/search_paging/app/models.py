from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=200,unique=True,default='IP')
    name = models.CharField(max_length=200,unique=True,default='Iphone')
    price = models.IntegerField(default=10)
    def __str__(self):
        return self.name