#base64_decode.py
import base64
#b1: Mở file lưu giữ code đã được mã hoá dạng string sau khi nhận từ json
f = open('img_encode.txt')
b64_text = f.read()
f.close()

#b2: làm theo b1 encode string trong file b2 decode data bytes
b64_data = b64_text.encode()
data = base64.b64decode(b64_data)

#b3: mở 1 file dạng jpg dạng ghi data lưu trữ
f = open('output.jpg','wb')
f.write(data)
f.close()