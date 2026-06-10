from flask import request, jsonify
from src.handlers.handlers import get_riders, get_riders_by_vehicle, create_review, update_review_comment, remove_rider, average_rating


def register_routes(app):

    @app.route("/riders")
    def riders():
        try:
            return jsonify(get_riders()), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @app.route("/riders/<vehicle>")
    def riders_by_vehicle(vehicle):
        try:
            result = get_riders_by_vehicle(vehicle)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
    
    @app.route("/reviews", methods=["POST"])
    def post_review():
        try:
            data = request.get_json()

            for field in ["rider_id", "customer_name", "rating"]:
                if field not in data:
                    return jsonify({"Error": f"Parametro {field} mancante"}), 400

            rider_id = data.get("rider_id")
            customer_name = data.get("customer_name")
            rating = data.get("rating")
            comment = data.get("comment")

            try:
                rating_int = int(rating)
            except ValueError:
                return jsonify({"Error": "rating deve essere un intero"}), 400

            if rating_int < 1 or rating_int > 5:
                return jsonify({"Error": "rating deve essere tra 1 e 5"}), 400

            review = create_review(
                rider_id,
                customer_name,
                rating_int,
                comment
            )

            return jsonify(review), 201

        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @app.route("/reviews/<int:id>", methods=["PUT"])
    def update_review(id):
        try:
            data = request.get_json()

            if "comment" not in data:
                return jsonify({"Error": "Parametro comment mancante"}), 400

            comment = data.get("comment")

            if not isinstance(comment, str) or not comment.strip():
                return jsonify({"Error": "comment deve essere una stringa valida"}), 400

            review = update_review_comment(
                id,
                comment.strip()
            )

            if review is None:
                return jsonify({"error": "Review not found"}), 404

            return jsonify(review), 200

        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @app.route("/riders/<int:id>", methods=["DELETE"])
    def delete_rider(id):
        try:
            rider = remove_rider(id)

            if rider is None:
                return jsonify({"Error": "rider not found"}), 404

            return jsonify({
                "message": "Rider deleted successfully",
                "deleted": rider
            }), 200

        except Exception as e:
            return jsonify({"Error": str(e)}), 500
    
    @app.route("/media/<int:rider_id>", methods=["GET"])
    def media(rider_id):
        try:
            result = average_rating(rider_id)

            if result is None:
                return jsonify({"error": "Rider not found or has no reviews"}), 404

            return jsonify(result), 200

        except Exception as e:
            return jsonify({"Error": str(e)}), 500
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "error": "Endpoint non trovato",
            "status": 404
        }), 404