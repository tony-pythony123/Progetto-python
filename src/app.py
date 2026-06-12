from flask import Flask
from src.routes import consegne_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(consegne_bp)

    return app