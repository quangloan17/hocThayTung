from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

#Truyền tham số trực tiếp qua link
@app.route('/hello') #localhost:5000
def hello():
    name = request.args.get('name','')
    gender = request.args.get('gender','')
    saluation = ''
    if gender == 'M': saluation = 'Mr'
    if gender == 'F': saluation = 'Ms'
    return f'Hello {saluation} {name}'

#Truyên tham số qua form
@app.route('/hello2',methods=['POST'])
def hello2():
    name = request.form.get('name','')
    gender = request.form.get('gender','')
    saluation = ''
    if gender == 'M': saluation = 'Mr'
    if gender == 'F': saluation = 'Ms'
    return f'Hello {saluation} {name}'

app.run(debug = True)

