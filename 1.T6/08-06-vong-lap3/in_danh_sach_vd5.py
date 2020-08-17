#VD05: Cho danh sách và 1 số
# Tìm phần tử trong danh sách gần nhất với số đã cho:

lst = [23,6,4,7,9,78]
x = int(input('Nhập số gần nhất: '))#32

imin = 0 #Thứ hạng phần tử nhỏ nhất
dmin = abs(x-lst[0]) #Số gần nhất với số đã cho là x

N = len(lst)
for i in range(N):
    di = abs(lst[i]-x)
    print('Thứ hạng i =',i,', di=',di)
    #Todo: New lst[i] gần x hơn lst[imin]--> imin = i
    if di < dmin:
        imin = i
        dmin = di

print('imin = ',imin,', dmin = ',dmin)
