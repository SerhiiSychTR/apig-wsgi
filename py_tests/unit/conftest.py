import pytest

from awsgi_poc.server.config import TestingConfig
from awsgi_poc.server.factory import create_app


@pytest.fixture
def app():
    TestingConfig.RESTPLUS_VALIDATE = False
    app = create_app(TestingConfig)
    return app
