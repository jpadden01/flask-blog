from . import Post, db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    if not current_user.is_authenticated:
        flash('Please log in first', category='warning')
        return redirect(url_for('auth.login'))
    return render_template('home.html')

@login_required
@routes.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        post = Post(
            title=request.form.get('title'),
            content=request.form.get('content'),
            user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created', category='success')
        return redirect('routes.home')
    return render_template('post.html')