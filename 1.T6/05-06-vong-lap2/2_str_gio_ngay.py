#Nhập vào ngày tháng theo format:dd/mm/yyyy HH:MM:SS
#In ra: ngày,tháng,năm
#Ví dụ: 05/06/2020 19:54:30--> Ngày 05, tháng 06, năm 2020

f = str('05/06/2020 19:54:30')
d = f.split(' ')
print(d)
date = d[0].split('/')
time = d[1].split(':')

print(date)
print(time)

print(f'Giờ: {time[0]}')
print(f'Phút: {time[1]}')
print(f'Giây: {time[2]}')
