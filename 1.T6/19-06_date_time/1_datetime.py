from datetime import date,timedelta

#Import thư viện timedelta để cộng ngày tháng

d1 = date.today()
print(d1)

d2 = date(2020,4,25)
d2 = d1.strftime("%d/%m/%Y") 
#Hàm chuyển định dạng format ngày tháng năm
print(d2)

#hàm weekday trả về thứ trong tuần
#thứ 2 tương ứng 0, chủ nhật tương ứng 6

from datetime import date
d = date(2020,4,26)
print(d.strftime('%d-%m-%Y'))

from datetime import datetime
dt1 = datetime.now()
print(dt1)

dt2 = datetime(2020,4,25,12,30,0)
print(dt2.strftime('%d-%m-%Y %H:%M:%S'))

# dt.year,dt.month,dt.day #gán nhiều biến để nhận giá trị
# dt.hour,dt.minute,dt.second
# dt + timedelta(days = 1) #Công thức cộng ngày, hoặc giờ, hoặc phút

#datetime.strptime('2020-06-01','%Y-%m-%d')