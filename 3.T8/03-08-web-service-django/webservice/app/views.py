from django.shortcuts import render,HttpResponse,redirect
import json


# Create your views here.
def index(request):
    return render(request,'index.html')

def hello(request):
    content = json.dumps({'message':'hello'})
    return HttpResponse(content,content_type='application/json')

productList = [
    {'code':'IPX','name':'Iphone X','price':17.5},
    {'code':'IP8','name':'Iphone 8','price':14.5},
    {'code':'IP7','name':'Iphone 7','price':10.5},
]

#Hàm GET.get để nhận số liệu từ đường link, có thể sử dụng để get thời gian rất tốt

def searchProduct(request):
    keyword = request.GET.get('keyword','')
    result = [p for p in productList if keyword in p['code']
                        or keyword in p['name']]
    return HttpResponse(json.dumps(result), content_type='application/json')
    