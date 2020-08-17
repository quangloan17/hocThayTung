from datetime import date
#Viết hoa và chữ thường phải chuẩn để biến biến thuộc loại gì
class Person:        
    def __init__(self,name,yob): #self để dữ liệu vào
        self.name = name #1 field trường thông tin 
        self.yob = yob

    def sayHello(self):
        print('Tên tôi là: ', self.name)
        
    def getAge(self):
        return date.today().year - self.yob + 1 #Nhận ngày và năm hiện tại - năm sinh + 1 năm

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


person = Person('Nguyễn Văn An',2000)
person.sayHello()
print(person.getAge())
print(person)