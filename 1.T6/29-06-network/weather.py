#Lấy thông tin dự báo thời tiết
import requests
import json

url = 'http://api.openweathermap.org/data/2.5/weather?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9'

resp =  requests.get(url)
obj = json.loads(resp.text)
print(obj)
print('Nhiệt độ Hà Nội hiện tại: ',obj['main']['temp'],'độ C')
print('Tốc độ gió Hà Nội hiện tại: ',obj['wind']['speed'])

