from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"

db = SQLAlchemy()

from .models import User, Post

from .routes import routes
from .auth import auth
app.register_blueprint(routes)
app.register_blueprint(auth)

db.init_app(app)
with app.app_context():
    db.create_all()