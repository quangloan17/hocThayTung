from django.shortcuts import render,HttpResponse,redirect
from .forms import ProductForm,CustomerForm
from .models import Product

# Create your views here.
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            context = {
                'fullname':form.cleaned_data['fullname'], #form.cleaned_data tương đương request.POST
                'phone':form.cleaned_data['phone'],
            }
            return render(request,'confirm.html',context)
    context = {'form':form}
    return render(request,'index.html',context)

def listProduct(request):
    productList = Product.objects.all().order_by('-id')
    totalPrice = sum(p.price for p in productList)
    context = {'productList':   productList,'totalPrice':totalPrice}
    return render(request,'product/list.html',context)
    
def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form':form}
    return render(request,'product/form.html',context)

def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance = product) # Có install sẽ lấy toàn bộ tham số của product chuyển về form
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES
                                ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form':form}
    return render(request,'product/form.html',context)

def deleteProduct(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('list-product')

