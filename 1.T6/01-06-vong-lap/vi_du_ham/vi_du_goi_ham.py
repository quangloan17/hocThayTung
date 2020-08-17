#In cac so binh phuong khi goi ham theo truong so lieu 1 -> 11
def square(x):
   return x*x
for i in range(1,11):
   print(square(

#Tinh dien tich va chu vi cua 1 hinh chu nhat khi biet do dai 2 canh
def calcAreaAndPerimeter(width, height):
    S = width * height
    P = 2*(width + height)
    return S, P

S, P = calcAreaAndPerimeter(5, 4)
print('S = ', S)
print('P = ', P)
