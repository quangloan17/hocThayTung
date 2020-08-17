import requests
html = requests.get('https://dantri.com.vn').text

with open('index.html', 'w', encoding='utf-8') as f:
   f.write(html)