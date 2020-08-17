#1. Todo: Tạo vòng lặp và gán thứ tự i,j trong mảng để kiểm tra số bằng 2 số trong mảng cộng lại
# arr = [1,2,3,4,12,5,7,13,8]
# a=b=c=0
# N = len(arr)
# for i in range(N):
#     a = arr[i]
#     for j in range(i+1,N):
#         b = arr[j]
#         c = b - a
#         if c in arr:
#             print(f'{c}={b}-{a}')

#1. Todo: Tạo vòng lặp và gán thứ tự i,j trong mảng để kiểm tra số bằng 2 số trong mảng cộng lại
# arr = [1,2,3,4,12,5,7,13,8]
# a=b=c=0
# N = len(arr)
# for i in range(N):
#     a = arr[i]
#     for j in range(i+1,N):
#         b = arr[j]
#         c = b - a
#         if c in arr:
#             print(f'{c}={b}-{a}')

#2. Todo: tính dân số Việt Nam:
danso = 20000
year = 2020
r = 1/100
#Dùng vòng lặp while để tìm số năm dân số đạt đến 50000
# while danso <= 50000:
#     year += 1
#     danso = danso *(1 + r)
#     print(year, round(danso,1))


for year in range(2020,2200):
    danso = danso * (1 + r)
    print(f'Đến năm: {year} có dân số: {round(danso,1)}')
    if danso >= 50000:
        break
    