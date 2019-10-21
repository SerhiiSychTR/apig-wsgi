import mock

from flask import url_for


class RequestResourceTest:
    partial_request_body = {"requestConfiguration": {"requestId": "test"}}

    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_200(self, get_response_by_request_id_mock, client):
        get_response_by_request_id_mock.return_value = {"hello": "Cham"}
        response = client.post(
            url_for("privacy_request"), json=self.partial_request_body
        )
        assert response.status_code == 200
        assert response.get_json() == {"hello": "Cham"}

    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_400(self, get_response_by_request_id_mock, client):
        get_response_by_request_id_mock.return_value = {}
        response = client.post(
            url_for("privacy_request"), json=self.partial_request_body
        )
        assert response.status_code == 400
        assert response.get_json() == {"error": "wrong request id"}
