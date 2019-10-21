import pytest


@pytest.fixture
def privacy_request_body():
    """Base request body for PrivacyRequest endpoint (POST method)"""
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
