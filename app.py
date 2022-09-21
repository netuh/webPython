from flask import Flask, render_template

app = Flask(__name__)

dicionario = {
    "neto": "123",
    "luis": "456"
}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/create/<first_name>/<last_name>')
def create(first_name='nome', last_name='nome2'):
    return 'Hello ' + first_name + ',' + last_name


@app.route("/login2")
def login2():
    return dicionario["luis"]


@app.route("/home")
def home():
    return render_template('home.html')
