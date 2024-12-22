from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/index/')
@app.route('/index/<name>')
def index(name=None):
    return render_template('index.html', person=name)

@app.route("/")
def hello_world():
    return "<p>Hello, je m'apelle Maxime, que puis-je faire pour toi?</p>"


@app.route("/<name>")
def name_hello(name):
    return f'<p>Hello, je m\'apelle {escape(name)}, que puis-je faire pour toi?</p>'