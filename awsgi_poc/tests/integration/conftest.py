import pytest

from awsgi_poc.server.factory import create_app
from awsgi_poc.server.config import TestingConfig


@pytest.fixture
def app():
    # hack to swtich of input request validation for unit testing
    app = create_app(TestingConfig)
    return app
