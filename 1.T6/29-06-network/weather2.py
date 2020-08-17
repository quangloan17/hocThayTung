#Lấy thông tin dự báo thời tiết
import requests
import json

url = 'http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8'
#b1. Gọi hàm get và truyền url vào hàm
resp =  requests.get(url) 
#2. Tạo obj nhận dữ liệu url truyền json về
obj = json.loads(resp.text) 
items = obj['list']
for item in items:
    print('Ngày: ', item['dt_txt'], 'nhiệt độ là: ', item['main']['temp'])


