import unittest

from awsgi_poc.server.apis.privacy.helper import get_response_by_request_id


class GetResponseByRequestIdTest(unittest.TestCase):
    def test_get_response_by_request_id(self):
        self.assertEqual(
            get_response_by_request_id("Serhii"), {"hello": "Serhii"}
        )
        self.assertEqual(get_response_by_request_id("Ivan"), {"hello": "Ivan"})
        self.assertEqual(get_response_by_request_id("Cham"), {"hello": "Cham"})

    def test_empty(self):
        self.assertEqual(get_response_by_request_id("wrong"), {})
