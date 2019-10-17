from awsgi_poc.server.privacy.namespace import privacy_ns
from awsgi_poc.server.privacy import resources

privacy_ns.add_resource(resources.Request, "/request")
