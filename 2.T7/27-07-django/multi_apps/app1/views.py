from django.shortcuts import render,HttpResponse

def hello1(request):
    if request.method == "GET":
        return render(request,'hello1.html')
    else:
        name = request.POST['name']
        return HttpResponse(f'Hello {name}')

def hello2(request):
    return HttpResponse('Xin chào bạn')