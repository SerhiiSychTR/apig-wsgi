from flask_testing import TestCase

from awsgi_poc.server.config import TestingConfig
from awsgi_poc.server.factory import create_app


class FlaskAppTestCase(TestCase):
    def create_app(self):
        TestingConfig.RESTPLUS_VALIDATE = False
        app = create_app(TestingConfig)
        return app
