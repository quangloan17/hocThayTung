#VD4:
#Cho 1 danh sách số
#In ra số lần xuất hiện của mỗi số trong danh sách

ds = [1,2,3,1,2,5,6,4,2,1,2,5]
#tạo 1 set để lọc phần từ trùng nhau
count={}

for x in ds:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
print(count)
