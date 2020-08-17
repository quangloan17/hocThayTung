#VD2:
#Nhập vào 1 ngày d dạng đd/mm/yyyy
#Nhập vào 1 số n
#In ra ngày d+n
from datetime import datetime,timedelta

d = input('Nhập ngày (dd/mm/yyyy): ')
n = int(input('Nhập số n: '))

#TODO: Convert d ==> date
d = datetime.strptime(d,'%d/%m/%Y')

#todo: Cộng d với n
d += timedelta(days = n)

#TODO: Format d theo dạng dd/mm/yyyy

print(d.strftime('%d/%m/%Y'))