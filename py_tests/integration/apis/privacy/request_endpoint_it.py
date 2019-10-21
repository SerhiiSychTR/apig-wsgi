import pytest
from flask import url_for


@pytest.fixture
def privacy_request_body_wrong_schema(privacy_request_body):
    """
    Request body for PrivacyRequest endpoint with error in schema:
    requestConfiguration.subTaskId has List instead of string
    """
    privacy_request_body["requestConfiguration"]["subTaskId"] = []
    return privacy_request_body


@pytest.fixture
def privacy_request_body_wrong_request_id(privacy_request_body):
    """
    Request body for PrivacyRequest endpoint with empty requestId:
    allowed values for requestConfiguration.requestId: Serhii, Ivan, Cham
    """
    privacy_request_body["requestConfiguration"]["requestId"] = ""
    return privacy_request_body


class RequestResourceIT:
    def test_200(self, privacy_request_body, client):
        response = client.post(
            url_for("privacy_request"), json=privacy_request_body
        )
        assert response.status_code == 200
        assert response.get_json() == {"hello": "Cham"}

    def test_400_wrong_schema(self, client, privacy_request_body_wrong_schema):
        response = client.post(
            url_for("privacy_request"), json=privacy_request_body_wrong_schema
        )
        expected_response = {
            "errors": {
                "requestConfiguration.subTaskId": "[] is not of type 'string'"
            },
            "message": "Input payload validation failed",
        }
        assert response.status_code == 400
        assert response.get_json() == expected_response

    def test_400_wrong_request_id(
        self, client, privacy_request_body_wrong_request_id
    ):
        response = client.post(
            url_for("privacy_request"),
            json=privacy_request_body_wrong_request_id,
        )
        assert response.status_code == 400
        assert response.get_json() == {"error": "wrong request id"}
