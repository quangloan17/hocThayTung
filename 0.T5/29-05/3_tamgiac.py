a = float(input('Nhập vào chiều dài cạnh 1: '))
b = float(input('Nhập vào chiều dài cạnh 2: '))
c = float(input('Nhập vào chiều dài cạnh 3: '))

if ((a + b > c) and (b + c > a) and (a + c > b) and a>0 and b>0 and c>0):
    print('Bạn nhập là hình tam giác')
else:
    print('Bạn nhập không phải hình tam giác')
