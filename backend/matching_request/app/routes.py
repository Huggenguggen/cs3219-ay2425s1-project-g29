from flask import Blueprint, request, jsonify

from .producer import publish_to_matching_queue

matching_bp = Blueprint(
    "matching",
    __name__,
)


@matching_bp.route("/matching", methods=["POST"])
def match_request():
    data = request.get_json()
    user_id = data.get("user_id")
    topic = data.get("topic")
    difficulty = data.get("difficulty")

    # add authentication

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    if not topic:
        return jsonify({"error": "topic is required"}), 400

    if not difficulty or difficulty not in ["easy", "medium", "hard"]:
        return (
            jsonify({"error": "difficulty must be one of 'easy', 'medium', or 'hard'"}),
            400,
        )

    message = {"user_id": user_id, "topic": topic, "difficulty": difficulty}
    error_response = publish_to_matching_queue(message)
    if error_response:
        return jsonify(error_response), 500

    return jsonify({"message": "User is queued for matching"}), 200
