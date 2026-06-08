from flask import Flask
from src.routes import magazzino_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(magazzino_bp)
    return app