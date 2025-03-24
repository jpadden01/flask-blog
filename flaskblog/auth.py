from . import db
from .models import User
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form.get('username')).first():
            flash('Username taken')
            return render_template('signup.html')
        if User.query.filter_by(email=request.form.get('email')).first():
            flash('Email already in use')
            return render_template('signup.html')
        if request.form.get('password') != request.form.get('password-confirm'):
            flash('Passwords do not match')
            return render_template('signup.html')
        user = User(
            username=request.form.get('username'),
            email=request.form.get('email'),
            password=request.form.get('password'),
            fname=request.form.get('fname'),
            lname=request.form.get('lname')
        )
        db.session.add(user)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('routes.home'))
    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user:
            if user.password != request.form.get('password'):
                flash('Incorrect password')
                return render_template('login.html')
            login_user(user)
            flash('Logged in succesfully')
            return redirect(url_for('routes.home'))
        flash('Email not registered for account')
    return render_template('login.html')