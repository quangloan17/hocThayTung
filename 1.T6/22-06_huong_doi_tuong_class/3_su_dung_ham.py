#Viết hoa và chữ thường phải chuẩn để biến biến thuộc loại gì
class Person:        
    def __init__(self,name,yob): #self để dữ liệu vào
        self.name = name #1 field trường thông tin 

    def sayHello(self):
        print('Tên tôi là: ', self.name)
        
    def __repr__(self):
        return self.name

class Student(Person):
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def sayHello(self):
        super().sayHello()
        print(f'Tôi học khoá: {self.course}') #Ghi đè phương thức đã tồn tại

st = Student('Nguyễn Văn An', 'Python 2005')
st.sayHello()
print([st])