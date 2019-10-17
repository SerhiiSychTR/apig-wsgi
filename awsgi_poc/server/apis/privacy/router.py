from awsgi_poc.server.apis.privacy.namespace import privacy_ns
from awsgi_poc.server.apis.privacy import resources

privacy_ns.add_resource(
    resources.Request, "/request", endpoint="privacy_request"
)
