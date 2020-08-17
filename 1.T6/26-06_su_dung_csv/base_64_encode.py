#base64_encode.py
import base64
#b1: Đọc file
f = open('test.jpg','rb') #rb là read dạng nhị phân (binary)
data = f.read()
f.close

# print(data.__class__,len(data)) #trả về số byte được in ra
# print(data)

#b2: encode là mã hoá dạng base64 trả về dạng bytes ko gửi đi được trên server
b64_data = base64.b64encode(data) #Mã hoá dạng b64 encode
print(b64_data)
print(b64_data.__class__,len(b64_data))

#b3: decode để chuyển sang string và gửi dạng json
b64_text = b64_data.decode() #decode để convert sang dạng string truyền đi
print(b64_text)
print(b64_text.__class__,len(b64_data))

#b4: Ghi vào file txt 
f = open('img_encode.txt','w')
f.write(b64_text)
f.close