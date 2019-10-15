from flask.cli import FlaskGroup

from awsgi_poc.server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def command_example():
    """Command example."""
    print("Command example")


if __name__ == "__main__":
    cli()
