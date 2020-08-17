products = [
        ('Iphone6', 6.0),
        ('Iphone7', 8.5),
        ('Galaxy S3', 6.5),
        ('Iphone 8', 12.0),
        ('Iphone X', 16.0),
        ('Iphone 11', 18.0),  
    ]
products = sorted(products,key = lambda x:x[1],reverse = True)
for p in products:
    print(p)
