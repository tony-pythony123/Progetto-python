from flask import jsonify
from src.handlers.product_handler import get_riders, get_reviews

# Scusate questo è un test per alberto
def register_routes(app):

    @app.route("/riders", methods=["GET"])
    def riders():
        return jsonify(get_riders())

    @app.route("/reviews", methods=["GET"])
    def reviews():
        return jsonify(get_reviews())