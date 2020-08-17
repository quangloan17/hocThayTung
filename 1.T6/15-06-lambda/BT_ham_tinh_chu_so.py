def tinh_chu_so(so_nguyen):
    lst = []
    so_nguyen = str(so_nguyen)
    tong = 0
    for a in so_nguyen:
        lst.append(int(a))
    for s in lst:
        tong += s
    return(tong)
so = input('Nhập số để tính chữ số: ')
tong = tinh_chu_so(so)
print('Tổng các chữ số trong số: ',tong)
