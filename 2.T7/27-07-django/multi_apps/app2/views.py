from django.shortcuts import render,HttpResponse

def hello3(request):
    return render(request,'hello3.html')
