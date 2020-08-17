products = [
        ('Iphone6', 6.0),
        ('Iphone7', 8.5),
        ('Galaxy S3', 6.5),
        ('Iphone 8', 12.0),
        ('Iphone X', 16.0),
        ('Iphone 11', 18.0),  
    ]
print(products)
#Todo: Chia sản phẩm thành 3 phân khúc: 5-10 triệu, 10-15 triệu, 15-20 triệu:
N1,N2,N3 = [],[],[]

for p in products:
    name,price = p #Tuple sinh ra để tách biến
    if price < 10:
        #Nhom1
        N1.append(p)
    elif price < 15:
        #Nhom 2
        N2.append(p)
    else:
        #Nhom 3
        N3.append(p)
        
print('Nhóm 1: ',N1)
print('Nhóm 2: ',N2)
print('Nhóm 3: ',N3)
