# VD3:
# Nhập vào 1 ngày d dạng dd/mm/yyyy
# Nhập vào 1 số n
# In ra ngày ngày sau d đúng n ngày
# không tính thứ 7, chủ nhật

from datetime import datetime,timedelta

d = input('Nhập ngày (dd/mm/yyyy): ')
n = int(input('Nhập số n: '))

#TODO: Convert d ==> date
d = datetime.strptime(d,'%d/%m/%Y')

while n > 0:
    d += timedelta(days = 1)
    #TODO: Nếu d không là T7, CN thì giảm n
    if d.weekday() < 5: n -= 1


print(d.strftime('%d/%m/%Y'))