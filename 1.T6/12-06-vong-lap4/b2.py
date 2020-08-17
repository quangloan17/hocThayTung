#Vidu1:
#Nhap vao 1 xau van ban
#In ra danh sach cac từ đơn (Ko trùng nhau)

st = '''Thời tiết Hà Nội những ngày gần
đây hay có mưa vào
buổi sáng và buổi buổi chiều tối'''

words = st.lower().split(' ')
print(set(words))
