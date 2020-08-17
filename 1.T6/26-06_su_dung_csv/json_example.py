import json

product = {
'name':'Iphone X', 'price': 15.0
}


#1. Hàm dumps để xuất ra string, đóng gói lại
print(product.__class__)
json_st = json.dumps(product)

#2. json_st đã chuyển sang biến dạng string
print(json_st)
print(json_st.__class__)

#3. Xuất ra file json để chuyển sang các hệ thống khác
with open('product.json','w') as f: 
    f.write(json_st)

 