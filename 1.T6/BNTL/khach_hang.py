khach_hang = [
    {'name':'Quang Nguyễn', 'age':30,'id_kh':1357},
    {'name':'Loan Nguyễn', 'age':30,'id_kh':1356},
    {'name':'Linh Nguyễn','age':15,'id_kh':1358},
]

don_hang = [
    {'date':'2020-03-10','san_pham':'Iphone X','price':12000,'qty':2,'id_kh_dh':1356},
    {'date':'2020-03-12','san_pham':'Iphone 6','price':15000,'qty':3,'id_kh_dh':1357},
    {'date':'2020-03-10','san_pham':'Iphone 7','price':11000,'qty':4,'id_kh_dh':1358},
    {'date':'2020-03-11','san_pham':'Iphone 8','price':10000,'qty':5,'id_kh_dh':1356},
]

chi_phi = [
    {'date':'2020-03-11','sp_mua_vao':'Iphone X','price':9000,'qty':2,'id_kh_cp':1357},
    {'date':'2020-03-10','sp_mua_vao':'Iphone 6','price':6000,'qty':2,'id_kh_cp':1356},
    {'date':'2020-03-08','sp_mua_vao':'Iphone 7','price':7000,'qty':2,'id_kh_cp':1356},
]

#Khởi tạo các dict
tongthu = {}
soluong = {}
tongchi = {}
loinhuan = {}
#Tính đơn hàng theo id khách hàng
for dh in don_hang:
    id_dh = dh['id_kh_dh']
    date = dh['date']
    sp = dh['san_pham']
    price = dh['price']
    qty = dh['qty']
    for kh in khach_hang:
        id_kh = kh['id_kh']
        name = kh['name']
        if id_kh == id_dh:
            tongthu[name] = tongthu.get(name,0) + price * qty   #Có thể nhận thêm giá trị ko???
            #todo: Thêm số lượng vào cùng dict tongthu[name] hay phải tách 1 dict riêng soluong[name]???
            soluong[name] = soluong.get(name,0) + qty

#Tính chi phí theo id khách hàng
for kh in khach_hang:
    id_kh = kh['id_kh']
    name = kh['name']
    if id_kh == id_dh:
        tongthu[name] = tongthu.get(name,0) + price * qty   #Có thể nhận thêm giá trị ko???
        #todo: Thêm số lượng vào cùng dict tongthu[name] hay phải tách 1 dict riêng soluong[name]???
        soluong[name] = soluong.get(name,0) + qty
    for cp in chi_phi:
        id_cp = cp['id_kh_cp']
        date = cp['date']
        price = cp['price']
        qty = cp['qty']
        
        if id_cp == id_kh:
            tongchi[name] = tongchi.get(name,0) + price * qty
            loinhuan[name] = tongthu[name] - tongchi[name]
        elif id_kh != id_cp:
            loinhuan[name] = tongthu[name]

#Kiểm tra các dict
print(tongthu.items())
print(tongchi.items())
print(soluong.items())
print(loinhuan.items())


print('-'*30)
print('TỔNG THU CỦA TỪNG KHÁCH')
for name in tongthu:
    print(name,' -> ',tongthu[name],'triệu')


print('-'*30)
print('TỔNG CHI CỦA TỪNG KHÁCH')
for name in tongchi:
    print(name,' -> ',tongchi[name],'triệu')

print('-'*30)
print('LỢI NHUẬN CỦA TỪNG KHÁCH')
for name in loinhuan:
    print(name,' -> ',loinhuan[name],'triệu')

print('-'*30)
print('TỔNG SỐ LƯỢNG BÁN/ KHÁCH')
for name in soluong:
    print(name,' -> ',soluong[name],'cái')


print('-'*30)
print('BẢNG THEO DÕI')
print('Tổng doanh thu: ',sum(tongthu.values()))
print('Tổng chi: ',sum(tongchi.values()))
print('Lợi nhuận:', sum(tongthu.values()) - sum(tongchi.values()))
print('Tổng số sp đã bán được: ', sum(soluong.values()), 'cái')
print('-'*30)
