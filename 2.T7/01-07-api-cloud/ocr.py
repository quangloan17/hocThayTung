import requests, json, base64

url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyATflEYmrT3Up1u7_fKc1bkddxV9Pt4P8Q'

#b1: Đọc hình ảnh sang dạng data base64 và trả về giá trị decode
def read_image(filename):
    with open(filename,'rb') as f:
        b64_data = base64.b64encode(f.read())
        return b64_data.decode()
    
#print(read_image('sample.jpg'))

#b2: Tạo file body để gửi dữ liệu lên server
for i in range(1,4):
    body = {
        "requests": [
            {
            'image': {"content":read_image(f'{i}.jpg')},
            'features':[{'type':'DOCUMENT_TEXT_DETECTION'}]
            }
        ]}

#b3: Gửi dữ liệu post lên server theo dạng string text trong body và lưu vào file với giá trị resp.text
    resp = requests.post(url,data = json.dumps(body))
# with open('result3.json','w',encoding = 'utf-8') as f:
#     f.write(resp.text)

#b4: Gọi giá trị obj và chuyển dữ liệu về dạng data qua hàm loads và in ra dữ liệu bên trong dict
    obj = json.loads(resp.text)
# print(obj['responses'][0]['fullTextAnnotation']['text'])

    with open(f'{i}.txt','w',encoding = 'utf-8') as f:
        f.write(obj['responses'][0]['fullTextAnnotation']['text'])
# a = obj['responses'][0]['fullTextAnnotation']['text']
# print(a.split(' '))
# print(len(a.split(' ')))

