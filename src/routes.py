from flask import request, jsonify
from src.handlers.handlers import get_riders, get_riders_by_vehicle, create_review

def register_routes(app):

    @app.route("/riders")
    def riders():
        return jsonify(get_riders())


    @app.route("/riders/<vehicle>")
    def riders_by_vehicle(vehicle):
        return jsonify(get_riders_by_vehicle(vehicle))
    
    @app.route("/reviews", methods=["POST"])
    def post_review():
        data = request.get_json()
    
        review = create_review(
            data.get("id"),
            data.get("rider_id"),
            data.get("customer_name"),
            data.get("rating"),
            data.get("comment")
        )
    
        return jsonify(review), 201