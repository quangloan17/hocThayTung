from django.shortcuts import HttpResponse,render


def index(request):
    return HttpResponse('Trang chủ')

#Sử dụng phương thức GET.get để truyền tham số qua link
def hello(request): #127.0.0.1:8000/hello?name=A&gender=M
    name = request.GET.get('name','') #Dấu ngoặc thứ 2 '' là để nhập giá trị mặc định, -> để trống
    gender = request.GET.get('gender','')
    salutation = ''
    if gender == 'M': salutation = 'Mr'
    if gender == 'F': salutation = 'Ms'
    context = {'salutation':salutation,'name':name}
    return render(request,'hello.html',context)

def search(request,ten,tuoi):
    return HttpResponse('Tìm ' + ten + '<br> Tuổi: ' +tuoi)

