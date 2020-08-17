from django.shortcuts import render,HttpResponse,redirect
from .forms import CategoryForm
from .models import Category

def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList':   categoryList}
    return render(request,'category/list.html',context)
    
def createCategory(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    context = {'form':form}
    return render(request,'category/form.html',context)

def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance = category) # Có install sẽ lấy toàn bộ tham số của product chuyển về form
    if request.method == "POST":
        form = CategoryForm(request.POST
                                ,instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    context = {'form':form}
    return render(request,'category/form.html',context)

def deleteCategory(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('list-category')

