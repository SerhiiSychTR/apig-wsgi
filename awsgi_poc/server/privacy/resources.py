from flask import request
from flask_restplus import Resource

from awsgi_poc.server.privacy.namespace import privacy_ns
from awsgi_poc.server.privacy.models import privacy_request_model


class Request(Resource):
    @privacy_ns.expect(privacy_request_model, validate=True)
    def post(self):
        request_id = request.json["requestConfiguration"]["requestId"]
        if request_id == "Cham":
            return {"hello": "Cham"}
        elif request_id == "Serhii":
            return {"hello": "Serhii"}
        elif request_id == "Ivan":
            return {"hello": "Ivan"}

        return {"error": "wrong request id"}, 400
