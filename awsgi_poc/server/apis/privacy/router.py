from awsgi_poc.server.apis.privacy import resources
from awsgi_poc.server.apis.privacy.namespace import privacy_ns

privacy_ns.add_resource(
    resources.RequestListApi, "/requests", endpoint="privacy_request_list"
)

privacy_ns.add_resource(
    resources.RequestApi, "/requests/<request_id>", endpoint="privacy_request"
)
