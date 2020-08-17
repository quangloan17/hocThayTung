from datetime import date,timedelta
#Cách này sai
# for y in range(2000,2100):
#     N = 366 if y % 4 == 0 else 365
#     T = 52 if N == 365 else 53
#     print(N,'==>', y,' có', T, 'ngày chủ nhật')

#Sửa
def getNumberOfSundays(y):
    d = date(y,1,1)
    n = 0
    while d.year == y:
        if d.weekday() == 6:
            n += 1
        d += timedelta(days = 1)
    return n

for i in range(2000,2100):
    if getNumberOfSundays(i) == 53:
        print(i)