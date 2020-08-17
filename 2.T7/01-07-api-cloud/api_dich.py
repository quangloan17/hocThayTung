''' chương trình dịch đoạn văn bản giữa 2 ngôn ngữ'''

import requests, json, base64

url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyDG5oE4fISZx4bMrusB68XiJ56urWZLI_k'

text = input('Nhập văn bản cần dịch: ')
#Sử dụng body (Đặt tên khác như data cũng được) để lưu dữ liệu lớn hơn 4 bytes
body = {
        'q': text,
        'source': 'vi',
        'target': 'en',
        'format': 'text'
}

headers = {"Content-Type" : "application/json"}
#Sử dụng post để gửi tham số lớn hơn 4 bytes dữ liệu
resp = requests.post(url,data = json.dumps(body))
#print(resp.text) #Lấy dạng sơ đồ cây chuyển sang trang jsonbeauty
obj = json.loads(resp.text)
#.text là dạng hàm giống .next
print(obj['data']['translations'][0]['translatedText']) #Lấy số 0 vì nó dạng list
