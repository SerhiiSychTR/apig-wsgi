from flask import jsonify, Blueprint, request

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/index")
def index():
    return jsonify({"response": "ok"})


@main_blueprint.route("/privacy/v1/request", methods=["POST"])
def privacy_request():
    request_id = request.json["requestConfiguration"]["requestId"]
    if request_id == "Cham":
        return jsonify({"hello": "Cham"})
    elif request_id == "Serhii":
        return jsonify({"hello": "Serhii"})
    elif request_id == "Ivan":
        return jsonify({"hello": "Ivan"})
    return jsonify({"error": "wrong request id"}), 400
