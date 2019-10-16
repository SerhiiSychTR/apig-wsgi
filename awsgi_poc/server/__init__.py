import os

from flask import Flask
from flask_restplus import Api

from awsgi_poc.server.privacy.request_api import request_api

api = Api()
api.add_namespace(request_api, path="/privacy/v2")


def create_app(script_info=None):
    # instantiate the awsgi_poc
    app = Flask(__name__)

    app_settings = os.getenv(
        "APP_SETTINGS", "awsgi_poc.server.config.ProductionConfig"
    )
    app.config.from_object(app_settings)
    api.init_app(app)

    # register blueprints
    from awsgi_poc.server.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
