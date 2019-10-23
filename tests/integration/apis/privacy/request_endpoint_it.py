from flask import url_for

from tests.integration.base import FlaskAppTestCase


def get_correct_request_body():
    correct_request_body = {
        "requestConfiguration": {
            "requestId": "Cham",
            "subTaskId": "",
            "subjectType": "",
            "dataPrivacyActId": "",
            "assetInsightId": "",
            "requestType": "",
        },
        "userData": {
            "userName": "",
            "firstName": "",
            "middleName": "",
            "lastName": "",
            "suffix": "",
            "emailAddress": "",
            "country": "",
            "zip": "",
            "address": "",
            "state": "",
            "city": "",
            "apartmentSuiteNumber": "",
            "ssn": "",
            "dateOfBirth": "",
            "telephoneNumber": "",
        },
    }
    return correct_request_body


class RequestResourceIT(FlaskAppTestCase):
    def test_200(self):
        request_body = get_correct_request_body()
        response = self.client.post(
            url_for("privacy_request_list"), json=request_body
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"hello": "Cham"})

    def test_400_wrong_schema(self):
        request_body = get_correct_request_body()
        request_body["requestConfiguration"]["subTaskId"] = []

        response = self.client.post(
            url_for("privacy_request_list"), json=request_body
        )
        expected_response = {
            "errors": {
                "requestConfiguration.subTaskId": "[] is not of type 'string'"
            },
            "message": "Input payload validation failed",
        }
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), expected_response)

    def test_400_wrong_request_id(self,):
        request_body = get_correct_request_body()
        request_body["requestConfiguration"]["requestId"] = ""

        response = self.client.post(
            url_for("privacy_request_list"), json=request_body
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "wrong request id"})
