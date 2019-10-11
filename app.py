import awsgi
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True


@app.route('/browse/hello')
def hello_world():
    return 'Hello World!'


@app.route('/')
def index():
    return jsonify(status=200, message='OK')


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
