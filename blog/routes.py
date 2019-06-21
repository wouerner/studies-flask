import os
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from blog import app, db
# from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from blog.models import User
# from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    # user = User.query.all()
    user = User(username='t', email='t')
    db.session.add(user)
    db.session.commit()

    return dump(user)

