from django.shortcuts import render,HttpResponse,redirect


# Create your views here.

def home(request):
    return render(request,'index.html')

#Các trường quan trọng. GET: Lấy query string, POST là để gửi dữ liệu, FILES để upload

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage() #Import tính năng File storage để thực hiện tính năng upload
def upload(request):
    file = request.FILES.get('img')
    if file and file.name != '':
        saved_path = fs.save('static/'+file.name,file)
        return redirect('/'+saved_path)
    else:
        return HttpResponse('No file upload')
    return render(request,'index.html')