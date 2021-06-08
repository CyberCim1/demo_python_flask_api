from __version__ import api_version
from flask import Blueprint
from flask_restplus import Api

class API:
    def __init__(self, namespace_list):
        api_title = 'Log API'
        api_description = 'API created to support learning how APIs work'
        api_url_prefix = '/api/v'+api_version[0:1]
        self.alert_status_v1_blueprint = Blueprint('v1', __name__, url_prefix=api_url_prefix)

        self.alert_status_v1_api =  Api(self.alert_status_v1_blueprint,
                                version=api_version,
                                title=api_title,
                                description=api_description,
                                validate=True,
                                ordered=True,)
        self.add_api_namespace(namespace_list)

    def add_api_namespace(self, namespace_list):
        for namespace in namespace_list:
            self.alert_status_v1_api.add_namespace(namespace)

    def get_blueprint(self):
        return self.alert_status_v1_blueprint
