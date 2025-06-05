import flask

from flask import Flask

app = Flask(__name__)

@app.route("/harry")
def hello_world():
    return "<p>Hello,World!</p>"

@app.route("/hello_harry")
def harry():
    return "<p>Hello,Harry!</p>"

app.run(debug=True)