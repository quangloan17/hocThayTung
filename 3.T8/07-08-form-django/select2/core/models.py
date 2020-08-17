from django.db import models

# Create your models here.


class Language(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Entry(models.Model):
    name = models.CharField(max_length=124)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Favourite Language")

    def __str__(self):
        return self.name

CATEGORY = {
    '':'',
    '':'',
    '':'',
}
class Khachhang(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class Donhang(models.Model):
    name = models.CharField(max_length=200)

class Donhangct(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
