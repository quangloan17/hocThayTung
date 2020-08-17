from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files.get('img')
    if file and file.filename:
        file.save('static/images/'+file.filename)
        return redirect('/static/images/'+file.filename)
    return 'No file'
app.run(debug=True)
#127.0.0.1:5000/static/test.txt