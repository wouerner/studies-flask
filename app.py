from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()

@app.route('/')
def hello_world():
    return users

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
