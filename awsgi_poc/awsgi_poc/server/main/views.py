from flask import jsonify, Blueprint

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return jsonify({"response": "ok"})
