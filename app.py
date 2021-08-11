from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><b><u><i>Hello, Devesh!</i></u></h1></b>"

