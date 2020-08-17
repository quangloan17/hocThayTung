from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=200)

# Sử dụng models.PROTECT là không cho phép xoá
# sử dụng models.DO_NOTHING là không liên đới
# sử dụng models.CASCADE là liên kết và xoá dữ liệu của nhau


#Khi đã có dữ liệu phải thêm null để tránh xung đột thiếu dữ liệu
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True) 
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    price = models.FloatField()

#Tạo hàm thêm sản phẩm ngay trong models cũng được:
def addProduct(code,name,price):
    product = Product(code=code,name=name,price=price)
    product.save()

#Sử dụng gọi hàm để tách riêng hàm to thành hàm con
def getProductlist():
    return Product.objects.all()

# Sử dụng câu lệnh if để kiểm tra trùng lặp trong database
if getProductlist().count() == 0:
    addProduct('IPX','Iphone X',17.5)
    addProduct('IP7','Iphone 7',8.5)
    addProduct('IP8','Iphone 8',12.5)

# Sử dụng để in ra dòng 
# for p in getProductlist():
#     print(p.code,p.name,p.price)
