from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Load DB credentials from Railway environment
DB_USER = os.environ.get("MYSQLUSER")
DB_PASSWORD = os.environ.get("MYSQLPASSWORD")
DB_HOST = os.environ.get("MYSQLHOST")
DB_NAME = os.environ.get("MYSQLDATABASE")
DB_PORT = os.environ.get("MYSQLPORT")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ✅ Define model first
class Contact(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(80), nullable=False)
    email  = db.Column(db.String(120), nullable=False)
    ph_num = db.Column(db.String(15), nullable=False)
    msg    = db.Column(db.String(500), nullable=False)
    date   = db.Column(db.String(25))

# ✅ Then call create_all()
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        try:
            entry = Contact(
                name  = request.form.get("name"),
                email = request.form.get("email"),
                ph_num= request.form.get("phone"),
                msg   = request.form.get("message"),
                date  = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            )
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"<h3 style='color:red;'>Error Occurred:</h3><pre>{e}</pre>", 500

    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

# Run the app (Railway will inject PORT)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
