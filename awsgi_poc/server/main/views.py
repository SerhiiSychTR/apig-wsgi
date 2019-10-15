from flask import jsonify, Blueprint, request

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return jsonify({"response": "ok"})


@main_blueprint.route("/privacy/v1/request", methods=["POST"])
def privacy_request():
    request_id = request.json["requestConfiguration"]["requestId"]
    if request_id == "test_ID":
        return jsonify({"response": "ok"})
    return jsonify({"error": "Invalid requestId"}), 400
