import pytest

from flask import url_for


@pytest.fixture
def request_body_wrong_request_id(correct_request_body):
    correct_request_body["requestConfiguration"]["requestId"] = ""
    return correct_request_body


@pytest.fixture
def request_body_wrong_schema(correct_request_body):
    correct_request_body["requestConfiguration"]["subTaskId"] = []
    return correct_request_body


class TestRequestResourceIT:
    """The same tests in class style"""

    def test_200(self, client, correct_request_body):
        response = client.post(
            url_for("privacy_request"), json=correct_request_body
        )
        assert response.status_code == 200
        assert response.json == {"hello": "Cham"}

    def test_400_wrong_schema(self, client, request_body_wrong_schema):
        response = client.post(
            url_for("privacy_request"), json=request_body_wrong_schema
        )
        assert response.status_code == 400
        assert response.json == {
            "errors": {
                "requestConfiguration.subTaskId": "[] is not of type 'string'"
            },
            "message": "Input payload validation failed",
        }

    def test_400_wrong_request_id(self, client, request_body_wrong_request_id):
        response = client.post(
            url_for("privacy_request"), json=request_body_wrong_request_id
        )
        assert response.status_code == 400
        assert response.json == {"error": "wrong request id"}
