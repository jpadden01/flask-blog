from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('home.html')