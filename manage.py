import os

from flask.cli import FlaskGroup

from awsgi_poc.server.factory import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    os.system("coverage run -m pytest -m unit")
    os.system("coverage html")


if __name__ == "__main__":
    cli()
