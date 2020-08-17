danso = 97.3
r = 1.1/100

#TODO: 
for nam in range(2021,2031):
    danso=danso*(1+ r)
    print(f'Dân số năm {nam} là {round(danso,1)}')#Làm tròn 1 dấu phẩy
