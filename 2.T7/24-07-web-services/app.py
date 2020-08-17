from flask import Flask,jsonify,request,render_template
#Phải import request để tìm kiếm tham số 
app = Flask(__name__)

@app.route('/api/hello') #127.0.0.1:5003/api/hello
def hello():
    return jsonify({'message':'Hello'})

productList = [
    {'code':'IPX','name':'Iphone X','price':17.5},
    {'code':'IP7','name':'Iphone 7','price':12.5},
    {'code':'IP8','name':'Iphone 8','price':15.5},
]
# Đặt tên riêng cho đường dẫn khác với tham số productList truyền vào
@app.route('/api/search_product')#127.0.0.1:5003/api/search_product
def searchProduct():
    keyword = request.args.get('keyword','')
    result = [p for p in productList
                if keyword in p['code']
                or keyword in p['name']]
    return jsonify({'productList':result})

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True,port=5002)
