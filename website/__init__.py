from flask import Flask
from flask_session import Session

from .site.routes import site
from .auth.routes import auth
from .settings.routes import settings

def init_app():
    app = Flask(__name__)
    # app.config["SECRET_KEY"] = "topsecret"
    
    # Configure session to use filesystem (instead of signed cookies)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    
    app.register_blueprint(site)
    app.register_blueprint(auth)
    app.register_blueprint(settings)
    
    return app