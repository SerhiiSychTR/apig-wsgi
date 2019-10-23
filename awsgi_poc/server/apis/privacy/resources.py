from flask import request
from flask_restplus import Resource

from awsgi_poc.server.apis.privacy import helper
from awsgi_poc.server.apis.privacy.models import privacy_request_model
from awsgi_poc.server.apis.privacy.namespace import privacy_ns


class RequestListApi(Resource):
    @privacy_ns.expect(privacy_request_model)
    def post(self):
        request_id = request.get_json()["requestConfiguration"]["requestId"]
        response_data = helper.get_response_by_request_id(request_id)
        if response_data:
            return response_data, 200
        return {"error": "wrong request id"}, 400

    def get(self):
        requests = helper.get_request_list()
        requests_json = [item.to_json() for item in requests]
        return requests_json, 200


class RequestApi(Resource):
    def get(self, request_id):
        item = helper.get_request(request_id)
        if item:
            return item.to_json(), 200
        return {}, 404

    def put(self, request_id):
        new_item = helper.edit_request(request_id, request.get_json())
        if new_item:
            return new_item.to_json(), 200
        return {}, 400

    def delete(self, request_id):
        deleted = helper.delete_request(request_id)
        if deleted:
            return {}, 200
        return {}, 404
