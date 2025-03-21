from flask import Flask

app = Flask(__name__)

from .models import User, Post

from .routes import routes
from .auth import auth
app.register_blueprint(routes)
app.register_blueprint(auth)