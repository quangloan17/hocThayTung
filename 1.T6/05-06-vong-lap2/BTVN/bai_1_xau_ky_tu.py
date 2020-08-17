so_ky_tu = input('Nhập số ký tự: ')
a=0
for x in so_ky_tu:
    if x.isalpha():
        a += 1     
        print(x)
print('Số ký tự trong chuỗi này:',a)
