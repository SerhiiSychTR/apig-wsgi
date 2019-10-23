from flask import Blueprint, request, jsonify

from awsgi_poc.server.apis.plain_privacy import helper

privacy_blueprint = Blueprint("privacy", __name__)


@privacy_blueprint.route("/plain_requests", methods=["POST"])
def create_request():
    created = helper.create_request(request.get_json())
    if created:
        return jsonify(created.to_json()), 200
    return jsonify({}), 400


@privacy_blueprint.route("/plain_requests", methods=["GET"])
def list_requests():
    requests = helper.get_request_list()
    requests_json = [item.to_json() for item in requests]
    return jsonify(requests_json), 200


@privacy_blueprint.route("/plain_requests/<request_id>", methods=["PUT"])
def edit_request(request_id: str):
    new_item = helper.edit_request(request_id, request.get_json())
    if new_item:
        return jsonify(new_item.to_json()), 200
    return jsonify({}), 400


@privacy_blueprint.route("/plain_requests/<request_id>", methods=["DELETE"])
def delete_request(request_id: str):
    deleted = helper.delete_request(request_id)
    if deleted:
        return jsonify({}), 200
    return jsonify({}), 404


@privacy_blueprint.route("/plain_requests/<request_id>", methods=["GET"])
def retrieve_request(request_id: str):
    item = helper.get_request(request_id)
    if item:
        return jsonify(item.to_json()), 200
    return jsonify({}), 404
