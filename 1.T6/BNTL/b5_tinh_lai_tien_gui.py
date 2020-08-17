#1. Todo: Tính lãi tiền gửi:
tiengui = 500
r = 12/100 #1 năm
kyhan = 1
sokyhan = 6
tietkiem = 10

for i in range(1,sokyhan + 1):
    tiengui = tiengui * (1 + r/12) + (kyhan * tietkiem)
    print(f'{round(tiengui,1)} sau ky han {i}')