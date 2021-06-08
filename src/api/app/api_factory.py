from api import API
from utils.database.db_base import db

'''    Here is where we put together all the api componets      '''
class Factory:
    def __init__(self):
        #-----------------------Testing---------------------------#
        from controllers.alert_controller import AlertController
        from routes.alert_router import AlertRouter, ns as alert_ns
        ctrl = AlertController()
        route = AlertRouter(ctrl)
        namespace_list = [alert_ns]
        #---------------------End Testing-------------------------#

        db_session = db.session

        api = API(namespace_list)
        self.v1_blueprint = api.get_blueprint()

    def get_blueprint(self):
        return self.v1_blueprint
