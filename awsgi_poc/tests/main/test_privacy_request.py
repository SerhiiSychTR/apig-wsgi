import pytest
from flask import url_for


@pytest.fixture
def correct_request_body():
    request_body = {
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
    return request_body


@pytest.fixture
def request_body_wrong_request_id(correct_request_body):
    correct_request_body["requestConfiguration"]["requestId"] = ""
    return correct_request_body


@pytest.fixture
def request_body_wrong_wrong_schema(correct_request_body):
    correct_request_body["requestConfiguration"]["subTaskId"] = []
    return correct_request_body


def test_privacy_request_200(client, correct_request_body):
    response = client.post(
        url_for("privacy_request_privacy_request"), json=correct_request_body
    )
    assert response.status_code == 200
    assert response.json == {"hello": "Cham"}


def test_privacy_request_400_wrong_schema(
    client, request_body_wrong_wrong_schema
):
    response = client.post(
        url_for("privacy_request_privacy_request"),
        json=request_body_wrong_wrong_schema,
    )
    assert response.status_code == 400
    assert response.json == {
        "errors": {
            "requestConfiguration.subTaskId": "[] is not of type 'string'"
        },
        "message": "Input payload validation failed",
    }


def test_privacy_request_400_wrong_request_id(
    client, request_body_wrong_request_id
):
    response = client.post(
        url_for("privacy_request_privacy_request"),
        json=request_body_wrong_request_id,
    )
    assert response.status_code == 400
    assert response.json == {"error": "wrong request id"}
