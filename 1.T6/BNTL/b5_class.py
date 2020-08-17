class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Tôi đang đi chơi")


a = Student('Quang',20)
print(a.name,a.age)
#a.sayHello()
