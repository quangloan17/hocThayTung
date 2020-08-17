#VD5:
#Nhập vào 1 văn bản
#In ra số lần xuất hiện mỗi từ đơn


st = input('Nhập vào 1 văn bản: ')
words = st.lower().split()
count = {}
for w in words:
    count[w] = count.get(w,0)+1 #count(w) là key, count.get(w,0) là value
for w in count:
    print(w, ':', count[w])
print(count)
