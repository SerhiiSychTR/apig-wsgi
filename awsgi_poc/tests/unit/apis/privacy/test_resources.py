import mock
import pytest

from flask import url_for


@pytest.fixture
def partial_request_body():
    return {"requestConfiguration": {"requestId": "test"}}


class TestRequestResource:
    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_200(
            self, get_response_by_request_id_mock, client, partial_request_body,

    ):
        get_response_by_request_id_mock.return_value = {"hello": "Cham"}
        response = client.post(
            url_for("privacy_request"), json=partial_request_body
        )
        assert response.status_code == 200
        assert response.json == {"hello": "Cham"}

    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_400(
            self, get_response_by_request_id_mock, client, partial_request_body
    ):
        get_response_by_request_id_mock.return_value = {}
        response = client.post(
            url_for("privacy_request"), json=partial_request_body
        )
        assert response.status_code == 400
        assert response.json == {"error": "wrong request id"}
