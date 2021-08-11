from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h6><b><u>Hello, World!</u></h6></b>"

