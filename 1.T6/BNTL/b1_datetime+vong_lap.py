#TODO: Hiển thị thứ cho ngày được chọn:
from datetime import datetime,date,timedelta

y = date.today().year
d = date(y,1,1)
N = 366 if y%4 == 0 else 365
i=0

#1. Dùng vòng lặp while để in ra 10 ngày tiếp theo trong năm
# while (i < 10):
#     d += timedelta(days = 1)
#     i+=1
#     print(i,d)


#2. Dùng vòng lặp for để in ra ngày
# for i in range(N):
#     d += timedelta(days = 1)
#     i += 1
#     if d.weekday() == 6:
#         print(i,d, d.weekday())
# print(y)
# print(d)
# print(N)

#3. TODO: Dùng vòng lặp để in ra ngày lẻ trong năm
# from datetime import datetime,date,timedelta

# y = date.today().year
# d = date(y,1,1)
# N = 366 if y%4 == 0 else 365

# for i in range(N):
#     d += timedelta(days = 1)
#     if d.day == 1 or d.day % 3 == 0:
#         print(d)

#4. TODO: Dùng vòng lặp để tính ngày 1,3,5,7,9 hàng tháng:

# from datetime import datetime,date,timedelta

# y = date.today().year
# d = date(y,1,1)
# N = 366 if y%4 == 0 else 365
# a = []

# for i in range(N):
#     d += timedelta(days = 24)
#     if d.day in range(1,10,2): #Ngày nằm trong trường bắt đầu = 5, kết thúc = 9, bước nhảy 2
#         a.append(d)
#         #print(d)
# print(a)

#5. TODO: Dùng vòng lặp để tính ngày 1,3,5,7,9 hàng tháng:

from datetime import datetime,date,timedelta

y = date.today().year
d = date(y,1,1)
N = 366 if y%4 == 0 else 365
a = []

for i in range(N):
    d += timedelta(days = 24)
    if d.day in range(1,10,2): #Ngày nằm trong trường bắt đầu = 5, kết thúc = 9, bước nhảy 2
        a.append(d)
        #print(d)
print(a)