from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root@localhost/contact_page'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    ph_num = db.Column(db.String(12), nullable = False)
    msg = db.Column(db.String(200), nullable = False)
    date = db.Column(db.String(12))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ['POST', 'GET'])
def contact():
    if request.method=='POST':
        '''add enrty to database'''

    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

app.run(debug=True)