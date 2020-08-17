#VD4:
#Cho 1 danh sách số
#In ra số lần xuất hiện của mỗi số trong danh sách

ds = [1,2,3,1,2,5,6,4,2,1,2,5]
#tạo 1 set để lọc phần từ trùng nhau
count={}

for x in ds:
    #if x not in count:
     #   count[x] = 1
    #else:
     #   count[x] += 1
    count[x] = count.get(x,0)+1
#Todo: In tho trình tự số lượng giảm dần:
count_items = count.items()
count_items = sorted(count_items,reverse=True, key=lambda x:x[1])
#Mặc định dict chỉ truy xuất key lên muốn truy xuất value ta phải sử dụng lambda để truy xuất value
for x,n in count_items:
    print(x, ':', n)
