#Nhập vào Password:
#Kiểm tra có hợp lệ:
#+ Có ít nhất 6 ký tự
#+ Có ít nhất 1 chữ số
#+ Có ít nhất 1 chữ cái

mk = input('Nhập mật khẩu: ')

N = len(mk)
co_chu_cai = False
co_chu_so = False

for c in mk:
    if c.isalpha():
        co_chu_cai = True
        break
for c in mk:
    if c.isdigit():
        co_chu_so = True
        break

if N < 6:
    print("MK phải có ít nhất 6 ký tự")

if not co_chu_cai:
    print('MK phait có ít nhất 1 chữ cái')

if not co_chu_so:
    print('MK phải có ít nhất 1 chữ số')

if N >= 6 and co_chu_cai and co_chu_so:
    print('MK hợp lệ')
