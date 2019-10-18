from awsgi_poc.server.apis.privacy.helper import get_response_by_request_id


def test_get_response_by_request_id():
    assert get_response_by_request_id("Serhii") == {"hello": "Serhii"}
    assert get_response_by_request_id("Ivan") == {"hello": "Ivan"}
    assert get_response_by_request_id("Cham") == {"hello": "Cham"}


def test_get_response_by_request_id_empty():
    assert get_response_by_request_id("wrong") == {}
