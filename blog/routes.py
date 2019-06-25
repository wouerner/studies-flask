import os
from flask import render_template, request, jsonify
from blog import app, db
from blog.models import User

@app.route("/", methods = ['GET'])
@app.route("/index", methods = ['GET'])
def index():
    return jsonify(hello='t')
    # return jsonify(hello=[i.serialize for i in User.query.all()])

@app.route("/user", methods = ['GET'])
def get():
    user = db.session.query(User).get(1)
    return jsonify(hello=user.serialize)

@app.route("/user", methods = ['POST'])
def post():
    username = request.form.get('username')
    email = request.form.get('email')

    user = User(username, email)

    db.session.add(user)
    db.session.commit()

    return jsonify(hello='Criado')

@app.route("/user/<user_id>", methods = ['DELETE'])
def delete(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return jsonify(hello='Exluido!')

