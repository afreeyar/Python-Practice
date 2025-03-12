from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    data_joined = db.Column(db.Date, default=datetime.now(timezone.utc))


def __repr__(self):
    return f'<User: {self.email}>'
