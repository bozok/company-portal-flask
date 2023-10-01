from flask import Flask

def init_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "topsecret"
    
    return app