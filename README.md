# Try to setup WSGI application

### aws_wsgi
`awsgi.response()` wraps Flask WSGI application and give's lambda 
compatible function on output
```python

import awsgi
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return jsonify(status=200, message='OK')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

```


### ALB Cloud Formation stack
To create CloudFormation stack:
```bash
cd zappa-overview
sceptre create dev
```
Creates Application Load Balancer, Lambda function, Role for lambda, 
lambda invoke permission for ALB, ALB lambda Target group.
Watch `zappa-overview/templates/main.yaml`

### Deploy lambda
To deploy(update) your lambda source code(Flask server):
```bash
make deploy lambda_name=retrieve_lambda_name_from_cloudformation_stack
```

After deploying, ALB public domain name accessible, so you can test your app.
Open http://{ALB_domain_name}/browse/hello

http://apig-wsgi-alb-104503537.eu-central-1.elb.amazonaws.com/ - 
already deployed example
### Run locally
To run tests locally activate your virtualenv and do the following:
```bash
pip install requirements-test.txt
pytest test_app.py
```