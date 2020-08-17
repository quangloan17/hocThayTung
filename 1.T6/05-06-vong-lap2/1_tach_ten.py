#todo:
#Nhập vào: họ, tên đệm, tên
#in ra: Họ và tên đầy đủ:

ho_ten = input('Tên đầy đủ của bạn là: ')#nguyen huy quang
arr = ho_ten.split()

print('Họ',arr[0])
print('Tên',arr[-1])
ten_dem = ''
N = len(arr)
print(N)
for i in range(1,N-1):
    ten_dem += arr[i] + ' '
print('Tên đệm: ', ten_dem)
