from flask import Flask, request,render_template

app = Flask(__name__)

#Truyền tham số qua đường link trực tiếp
@app.route('/hello')  # http://localhost:5000?name=A&gender=M
def hello():
    name = request.args.get('name','world') #Trong ngoặc là key và value trong dict được truyền vào
    gender = request.args.get('gender')
    salutation = ''
    # return f'Hello {name}'
    if gender == 'M': salutation = 'Mr'
    if gender == 'F': salutation = 'Ms'
    #context = {'salutation':salutation,'name':name}
    return render_template('hello.html',salutation=salutation,name=name)
    #Tham số được truyền thẳng từ url vào trong template để xử lý render


#Truyền tham số qua input từ index
@app.route('/')    
def index():
    return render_template('index.html')
    

#Render template Không truyền tham số
@app.route('/hello2')  # http://localhost:5000
def hello2():
    return render_template('hello2.html')
    
app.run(debug=True)