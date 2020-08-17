#VD06: 
# Cho 2 danh sách số
# Tìm cặp phần tử của 2 danh sách
# Có khoảng cách gần nhất:

lst1 = [23,4,6,7,35,9,78]
lst2 = [10,20,30]

imin = 0
jmin = 0
dmin = abs(lst1[0]-lst2[0])
print('di-j min[0]: ',dmin)

for i in range(len(lst1)):
    for j in range(len(lst2)):
        dij = abs(lst1[i]-lst2[j])
        print('Thứ hạng i =',i,', Thứ hạng j =',j,', di-j=',dij)
        if dij < dmin: #dmin = 13 vậy lên dij < 13 là đúng bao gồm (dij = 3,7,6,4,3,5,1,11)
            imin = i
            jmin = j
            dmin = dij

print('lst1[imin]: ',lst1[imin],', lst2[jmin]: ',lst2[jmin],', di-j min nho nhat: ', dmin)
