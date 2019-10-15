import pytest
from flask import url_for


def test_home(client):
    r = client.get("/")

    assert r.status_code == 200
    assert r.json == {"response": "ok"}


@pytest.fixture
def correct_request_body():
    request_body = {
        "requestConfiguration": {
            "requestId": "test_ID",
            "subTaskId": [],
            "subjectType": {},
            "dataPrivacyActId": {},
            "assetInsightId": [],
            "requestType": {},
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
def wrong_request_body():
    request_body = {
        "requestConfiguration": {
            "requestId": "",
            "subTaskId": [],
            "subjectType": {},
            "dataPrivacyActId": {},
            "assetInsightId": [],
            "requestType": {},
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


def test_privacy_request_ok(client, correct_request_body):
    r = client.post(url_for("main.privacy_request"), json=correct_request_body)

    assert r.status_code == 200
    assert r.json == {"response": "ok"}


def test_privacy_request_400(client, wrong_request_body):
    r = client.post(url_for("main.privacy_request"), json=wrong_request_body)

    assert r.status_code == 400
    assert r.json == {"error": "Invalid requestId"}