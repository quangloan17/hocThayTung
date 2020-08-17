sale_orders = [
    {'name':'iphone X', 'price': 15.0,'qty':2,'date':'2020-06-01'},
    {'name':'iphone 11', 'price': 18.5,'qty':1,'date':'2020-06-01'},
    {'name':'iphone 8', 'price': 12.0,'qty':2,'date':'2020-06-03'},
    {'name':'Samsung S3', 'price': 6.5,'qty':1,'date':'2020-06-02'},
    {'name':'Samsung X', 'price': 15.5,'qty':2,'date':'2020-06-03'},
    ]
#tính doanh thu theo ngày
revenues = {}
for od in sale_orders:
    product = od['name']
    qty = od['qty']
    price = od['price']
    date = od['date']
    revenues[date] = revenues.get(date,0)+ qty*price
    
#Thống kế theo sản phẩm thì key là sản phẩm
items = sorted(revenues.items())
for date,revenue in items:
    print(date,':', revenue)
