from unittest import mock

from flask import url_for

from tests.unit.base import FlaskAppTestCase


class RequestResourceTest(FlaskAppTestCase):
    partial_request_body = {"requestConfiguration": {"requestId": "test"}}

    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_200(self, get_response_by_request_id_mock):
        get_response_by_request_id_mock.return_value = {"hello": "Cham"}
        response = self.client.post(
            url_for("privacy_request"), json=self.partial_request_body
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"hello": "Cham"})

    @mock.patch(
        "awsgi_poc.server.apis.privacy.helper.get_response_by_request_id"
    )
    def test_400(self, get_response_by_request_id_mock):
        get_response_by_request_id_mock.return_value = {}
        response = self.client.post(
            url_for("privacy_request"), json=self.partial_request_body
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "wrong request id"})
