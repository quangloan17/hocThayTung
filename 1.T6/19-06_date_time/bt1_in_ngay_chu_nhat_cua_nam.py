#VD1: In ra các ngày chủ nhật của năm nay

from datetime import date,timedelta

y = date.today().year
d = date(y,1,1)

N = 366 if y%4 == 0 else 365

#1. Dùng for
for i in range(N):
    d += timedelta(days = 1)
    if d.weekday() == 6:
        print(d)
   
    #TODO: Kiểm tra d có là chủ nhật:
    #TODO: Tăng d thêm 1

#2. Dùng while:
while d.year == y:
    if d.weekday() == 6:
        print(d)
    d += timedelta(days = 1)