import os
from flask import render_template, request, jsonify
from blog import app, db
from blog.models import User

@app.route("/", methods = ['GET'])
@app.route("/index", methods = ['GET'])
def index():
    return jsonify(data=[i.serialize for i in User.query.all()])

@app.route("/user/<user_id>", methods = ['GET'])
def get(user_id):
    user = db.session.query(User).get(user_id)
    return jsonify(hello=user.serialize)

@app.route("/user", methods = ['POST'])
def post():
    username = request.form.get('username')
    email = request.form.get('email')

    user = User(username, email)

    db.session.add(user)
    db.session.commit()

    return jsonify(hello='Criado!')

@app.route("/user/<user_id>", methods = ['PUT'])
def update(user_id):
    user = User.query.get_or_404(user_id)

    user.username = request.form.get('username')
    user.email = request.form.get('email')

    db.session.commit()

    return jsonify(hello='Atualizado!')

@app.route("/user/<user_id>", methods = ['DELETE'])
def delete(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return jsonify(hello='Exluido!')
