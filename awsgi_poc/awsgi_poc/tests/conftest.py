import pytest

from awsgi_poc.server import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
