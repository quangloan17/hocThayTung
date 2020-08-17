#write_csv.py
products = [
    {
        'code':'IP7',
        'name':'Iphone 7',
        'price':7.5
    },
    {
        'code':'IP8',
        'name':'Iphone 8',
        'price':8.5
    },
    {
        'code':'S3',
        'name':'Samsung S3',
        'price':6.5
    },

]

import csv
header_row = [
    'Code','Name','Price'
]


with open('output.csv','w', newline = '') as f:
    writer = csv.writer(f) #Writer giống 1 đối tượng container bọc file chúng ta ở bên trong
    writer.writerow(header_row)
    for p in products:
        data_row = [p['code'],p['name'],p['price']]
        writer.writerow(data_row)
