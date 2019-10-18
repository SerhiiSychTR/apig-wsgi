from flask.cli import FlaskGroup

from awsgi_poc.server.factory import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)



if __name__ == "__main__":
    cli()
