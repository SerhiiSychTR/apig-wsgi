import pytest

from awsgi_poc.server.config import TestingConfig
from awsgi_poc.server.factory import create_app


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    return app
