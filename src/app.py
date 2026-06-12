from flask import Flask, jsonify
from src.routes import consegne_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(consegne_bp)

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "error": "Endpoint non trovato",
            "status": 404
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({
            "error": "Metodo non consentito per questo endpoint",
            "status": 405
        }), 405

    return app