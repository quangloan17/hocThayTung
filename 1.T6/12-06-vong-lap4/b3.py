#VD2
#Nhập vào 2 xâu
#In ra chỉ số tương đồng:
#sim(st1,st2) = n(I),n(U)

#I: Tập hợp các từ chung
#U: tập hợp các từ thuộc
#1 trong 2 câu

st1 = input('Văn bản 1: ')
st2 = input('Văn bản 2: ')
s1 = set(st1.lower().split())
s2 = set(st2.lower().split())
#Todo: Dùng Intersection() tìm I
# Dùng union() tìm U

U = s1.union(s2)
I = s1.intersection(s2)
print(U)
print(I)
print('similarity=', len(I)/len(U))