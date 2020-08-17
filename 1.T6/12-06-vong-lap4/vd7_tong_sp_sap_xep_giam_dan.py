sale_orders = [
        {'product':'IPX','qty':2},
        {'product':'IP8','qty':1},
        {'product':'IP11','qty':1},
        {'product':'IP8','qty':2},
        {'product':'S3','qty':2},
        {'product':'IPX','qty':1},
    ]

#Todo: In ra số lượng bán của mỗi sản phẩm
#Sắp xếp theo thứ tự giảm dần
count = {}
for od in sale_orders:
    product = od['product']
    qty = od['qty']
    count[product] = count.get(product,0) + qty

#todo: Sắp xếp theo số lượng giảm dần:
count_items = sorted(count.items(),reverse=True, key = lambda x:x[1])
for p,qty in count_items:
    print(p,':', qty)
