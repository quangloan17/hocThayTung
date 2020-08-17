s = str(input("Nhập xâu: "))
dem = 0
for i in s:
    if i.isalpha():
        dem += 1
    else:
        continue
print("Số chữ cái trong xâu là:",dem)
