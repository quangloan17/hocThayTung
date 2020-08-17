import os

#Lấy danh sách file trong thư mục máy mac, máy window phải là C:\\
forder = '/Users'

#1. Hàm lisdir lấy danh sách các file trong thư mục
items = os.listdir(forder)
print('Danh sách file:')

#2. Hàm is file để hiển thị dạng file
# for item in items:
#     path = forder + item
#     if os.path.isfile(path):
#         print(path)

#3. Hàm join để kết hợp tên thư mục và tên file
files = [f for f in items if os.path.isfile(os.path.join(forder, f))]
print(files)