from awsgi_poc.server.apis.privacy import resources
from awsgi_poc.server.apis.privacy.namespace import privacy_ns

privacy_ns.add_resource(
    resources.Request, "/request", endpoint="privacy_request"
)
