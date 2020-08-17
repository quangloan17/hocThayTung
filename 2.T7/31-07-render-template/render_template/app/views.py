from django.shortcuts import render,HttpResponse,redirect

productList = [
    {'code':'IPX','name':'Iphone X','price':17.5},
    {'code':'IP8','name':'Iphone 8','price':14.5},
    {'code':'IP7','name':'Iphone 7','price':10.5},
]


# Create your views here.
def home(request):
    context = {'productList':productList}
    return render(request,'index.html',context)
    
def addProduct(request):
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        price = request.POST.get('price')
        productList.append({
            'code':code,'name':name,'price':price
        })
        return redirect('home')
    return render(request,'form.html')