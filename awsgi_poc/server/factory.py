import os

from flask import Flask
from flask_restplus import Api

api = Api()


def create_app(script_info=None):
    # instantiate the awsgi_poc
    app = Flask(__name__)

    app_settings = os.getenv(
        "APP_SETTINGS", "awsgi_poc.server.config.ProductionConfig"
    )
    app.config.from_object(app_settings)
    api.init_app(app)

    # register apis
    from awsgi_poc.server.privacy import privacy_ns
    api.add_namespace(privacy_ns, path="/privacy/v1")

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app