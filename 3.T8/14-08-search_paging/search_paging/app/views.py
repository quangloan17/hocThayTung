from django.shortcuts import render,HttpResponse,redirect
from .models import Product
from django.db.models import Q
import math

def getPriceValueRange(priceRange):
    if priceRange == '':return None,None
    if priceRange == '1':return None,10
    if priceRange == '2':return 10,15
    if priceRange == '3':return 15,None

# Create your views here.
def index(request):
    #Tạo phân trang
    PAGE_SIZE = 5
    page = int(request.GET.get('page',1))
    start = PAGE_SIZE * (page-1)
    end = start + PAGE_SIZE

    #Bắt từ khoá để tìm kiếm
    keyword = request.GET.get('keyword', '')
    priceRange = request.GET.get('priceRange','')

    #Nhận giá trị lớn nhỏ
    minPrice,maxPrice = getPriceValueRange(priceRange)

    #Filter theo toán tử lọc or not 1 trong 2 điều kiện đáp ứng
    productList = Product.objects.filter(
        Q(name__contains=keyword) | Q(code__contains=keyword))


    if minPrice:
        productList = productList.filter(price__gte = minPrice)
    if maxPrice:
        productList = productList.filter(price__lte = maxPrice)

    total = len(productList)
    num_page = math.ceil(total/PAGE_SIZE)

    totalPrice = sum([p.price for p in productList[start:end]])

    context = {
        'productList':productList[start:end],
        'keyword':keyword,
        'priceRange':priceRange,

        'start':start,
        'nextPage':page+1,
        'prePage':page-1,
        'total':total,
        'num_page':num_page,
        }
    return render(request,'index.html',context)

# Sử dụng toán tử Q để bổ sung điều kiện tìm kiếm or not
