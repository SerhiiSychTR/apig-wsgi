from flask import request
from flask_restplus import Resource

from awsgi_poc.server.apis.privacy.namespace import privacy_ns
from awsgi_poc.server.apis.privacy.models import privacy_request_model
from awsgi_poc.server.apis.privacy import helper


class Request(Resource):
    @privacy_ns.expect(privacy_request_model)
    def post(self):
        request_id = request.json["requestConfiguration"]["requestId"]
        response_data = helper.get_response_by_request_id(request_id)
        if response_data:
            return response_data, 200
        return {"error": "wrong request id"}, 400
