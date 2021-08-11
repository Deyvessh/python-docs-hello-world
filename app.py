from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><b><u><i>Hello, az104webapp1</i></u></h1></b>"

