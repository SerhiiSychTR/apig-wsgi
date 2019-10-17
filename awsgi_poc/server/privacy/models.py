from flask_restplus import fields

from awsgi_poc.server.privacy.namespace import privacy_ns

privacy_request_model = privacy_ns.model(
    "PrivacyRequest",
    {
        "requestConfiguration": fields.Nested(
            privacy_ns.model(
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
            privacy_ns.model(
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
