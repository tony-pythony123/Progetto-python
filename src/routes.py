from flask import request, jsonify
from src.handlers.handlers import get_riders, get_riders_by_vehicle, create_review, update_review_comment, remove_rider, media_consegne


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
    
    @app.route("/reviews/<int:id>", methods=["PUT"])
    def update_review(id):
        data = request.get_json()

        review = update_review_comment(
            id,
            data.get("comment")
        )

        if review is None:
            return jsonify({"error": "Review not found"}), 404

        return jsonify(review), 200
    
    @app.route("/riders/<int:id>", methods=["DELETE"])
    def delete_rider(id):
        rider = remove_rider(id)

        if rider is None:
            return jsonify({"Error": "rider not found"}), 404
        return jsonify ({
            "message":"Rider deleted succesfully",
            "deleted": rider
        }), 200
    
    @app.route("/media", methods=["GET"])
    def media():
        return jsonify(media_consegne())
