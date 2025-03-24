from . import db
from .models import User
from flask import Blueprint, render_template, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User(
            username=request.form.get('username'),
            email=request.form.get('email'),
            password=request.form.get('password'),
            fname=request.form.get('fname'),
            lname=request.form.get('lname')
        )
        flash('Account created!')
    return render_template('signup.html')

@auth.route('/login')
def login():
    return render_template('login.html')