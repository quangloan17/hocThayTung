from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

def addProduct(code, name, price):
    product = Product(code, name, price)
    db.session.add(product)
    db.session.commit()

def getProductList():
    return Product.query.order_by(Product.id.desc())

@app.route('/')
def index():
    return render_template('index.html',
            productList=getProductList())


def validate(form):
    errorList = []
    if not form.get('code'):
        errorList.append('Mã sản phẩm không được trống')
    if not form.get('name'):
        errorList.append('Tên sản phẩm không được trống')
    if not form.get('price').isdigit():
        errorList.append('Số tiền không hợp lệ')
    #SELECT count(*) FROM product where code = form['code']
    if Product.query.filter_by(code=form['code']).count() > 0:
        errorList.append('Mã sản phẩm đã tồn tại')
    return errorList

@app.route('/create_product', methods=['GET', 'POST'])
def createProduct():
    errorList = []
    form = {}
    if request.method == 'POST':
        form = request.form
        errorList = validate(form)
        if len(errorList) == 0:
            code = form.get('code')
            name = form.get('name')
            price = form.get('price')
            addProduct(code, name, price)
            return redirect('/')

    return render_template('form.html',
                errorList=errorList,
                form=form)

@app.route('/delete_product/<id>')
def deleteProduct(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/')

@app.route('/update_product/<id>',methods=['GET','POST'])
def updateProduct(id):
    form = Product.query.get(id)
    if request.method == 'POST':
        form.code = request.form['code']
        form.name = request.form['name']
        form.price = request.form['price']
        db.session.commit()
        return redirect('/')
    return render_template('form.html',form=form)

db.create_all()    
app.run(debug=True,port = 5002)
