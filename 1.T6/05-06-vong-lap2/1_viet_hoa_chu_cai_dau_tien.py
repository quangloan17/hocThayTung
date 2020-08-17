#todo:
#Nhập vào: họ, tên đệm, tên
#in ra: Họ và tên đầy đủ:

ho_ten = input('Tên đầy đủ của bạn là: ')
arr = ho_ten.split()
#todo: Viết hoa chữ cái đầu:

st = ''

for x in arr:
    xnorm = x[0].upper() + x[1:]
    st += xnorm + ' '
    print(st)
