#Viết hoa và chữ thường phải chuẩn để biến biến thuộc loại gì
class Person:        
    def __init__(self,name): #self để dữ liệu vào
        self.name = name #1 field trường thông tin  
        
person = Person('Nguyễn Văn An') #Tạo 1 instance và truyền vào đối tượng và biến số
print(person.name)