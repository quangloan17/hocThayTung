#Nhập vào ngày tháng theo format:dd/mm/yyyy
#In ra: ngày,tháng,năm
#Ví dụ: 05/06/2020 --> Ngày 05, tháng 06, năm 2020

d = input('Ngày hôm nay: ')
c = d.split('/')
print(f'Ngày: {c[0]}')
print(f'Tháng: {c[1]}')
print(f'Năm: {c[2]}')
