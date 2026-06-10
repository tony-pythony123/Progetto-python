from flask import jsonify
from src.handlers.product_handler import get_riders, get_reviews
from src.handlers.new_handler import media_consegne

# Scusate questo è un test per alberto
def register_routes(app):

    @app.route("/riders", methods=["GET"])
    def riders():
        return jsonify(get_riders())

    @app.route("/reviews", methods=["GET"])
    def reviews():
        return jsonify(get_reviews())
    
    @app.route("/media", methods=["GET"])
    def media():
        return jsonify(media_consegne())