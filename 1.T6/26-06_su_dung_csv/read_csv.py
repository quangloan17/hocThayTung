#read_csv.py
import csv

#Nếu ta dùng tiếng việt thì sử dụng utf-8 tại đây
with open('products.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    data_rows = list(reader)
#1. Ở đây sử dụng 3 hàm reader() đọc csv,
# next() để tiến đến dòng tiếp
# list() để tạo danh sách cho biến reader
print(header_row)
for row in data_rows:
    print(row)