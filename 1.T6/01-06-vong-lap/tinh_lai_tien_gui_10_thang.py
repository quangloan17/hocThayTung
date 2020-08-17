sotien = 100
kyhan = 1
sokyhan = 1
laisuat = 10 #10%/năm phai chia 12 thang de tinh lai 1 thang


#Ls 6 thang voi kỳ hạn 1 nam (2 ky han)
tyle_loinhuan = kyhan * laisuat/12/100
print(f'Tỷ lệ loi nhuan: {tyle_loinhuan}')
for a in range(1,sokyhan+1):
    sotien = sotien * (1 + tyle_loinhuan) + kyhan
    print(f'Số tiền sau kỳ hạn {a}: {round(sotien)} tr VND')
