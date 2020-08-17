tien_vay = 400
tra_hang_thang = 4
r = 10/12/100 #Tỷ lệ lai phai tra 10% 1 nam 
T = 0
while tien_vay > 0:
    T+=1
    if T == 1:
        tien_vay = tien_vay - tra_hang_thang #Cong thuc thay doi tang theo nam (1+r)
    else:
        tien_vay = tien_vay * (1+r) - tra_hang_thang #Cong thuc thay doi tang theo nam (1-r)    
    print(f' so tien {round(tien_vay,2)} tr VND trong thang {T}')
