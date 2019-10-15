import awsgi

from awsgi_poc.server import create_app

app = create_app()


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
