from flask import request
from flask_restplus import Namespace, fields, Resource

request_api = Namespace(
    "privacy_request", description="Privacy request related operations"
)

privacy_request_model = request_api.model(
    "PrivacyRequest",
    {
        "requestConfiguration": fields.Nested(
            request_api.model(
                "requestConfiguration",
                {
                    "requestId": fields.String(required=True),
                    "subTaskId": fields.String(required=True),
                    "subjectType": fields.String(required=True),
                    "dataPrivacyActId": fields.String(required=True),
                    "assetInsightId": fields.String(required=True),
                    "requestType": fields.String(required=True),
                },
            ),
            required=True,
        ),
        "userData": fields.Nested(
            request_api.model(
                "userData",
                {
                    "userName": fields.String(required=True),
                    "firstName": fields.String(required=True),
                    "middleName": fields.String(required=True),
                    "lastName": fields.String(required=True),
                    "suffix": fields.String(required=True),
                    "emailAddress": fields.String(required=True),
                    "country": fields.String(required=True),
                    "zip": fields.String(required=True),
                    "address": fields.String(required=True),
                    "state": fields.String(required=True),
                    "city": fields.String(required=True),
                    "apartmentSuiteNumber": fields.String(required=True),
                    "ssn": fields.String(required=True),
                    "dateOfBirth": fields.String(required=True),
                    "telephoneNumber": fields.String(required=True),
                },
            ),
            required=True,
        ),
    },
)


@request_api.route("/request")
class PrivacyRequest(Resource):
    @request_api.expect(privacy_request_model, validate=True)
    def post(self):
        request_id = request.json["requestConfiguration"]["requestId"]
        if request_id == "Cham":
            return {"hello": "Cham"}
        elif request_id == "Serhii":
            return {"hello": "Serhii"}
        elif request_id == "Ivan":
            return {"hello": "Ivan"}

        return {"error": "wrong request id"}, 400
