#VD4:
#Cho 1 danh sách số
#In ra số lần xuất hiện của mỗi số trong danh sách

ds = [1,2,3,1,2,5,6,4,2,1,2,5]
#tạo 1 dict để lọc phần từ trùng nhau
count={}

for x in ds:
    count[x] = count.get(x,0)+1 #ở đây key = 1, value mặc định = 0 nếu x = 1 
    #=> Đây là phép gán giá trị vào dict
    #if x not in count:
     #   count[x] = 1
    #else:
     #   count[x] += 1
for x in count:
    print(x, ':', count[x])
