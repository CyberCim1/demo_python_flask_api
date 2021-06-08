from utils.http_response_codes import HTTPStatus
from flask_restplus import abort
from . import AbstractController

class AlertController(AbstractController):
    def __init__(self):
        self.counter = 0
        self.systems = []

    #TODO: Consider creating a error response file for each table and a BaseValidator file
    def abort_if_alert_doesnt_exist(self, alert_id):
        msg ="No alerts doesn't exist."
        if(id != 0):
            msg = "Alert {} doesn't exist".format(id)
        abort(HTTPStatus.NOT_FOUND, message=msg)

    def get_all(self):
        return self.systems

    def get(self, id):
        for system in self.systems:
            if system['id'] == id:
                print('Get funcion:',system['id'], id)
                return system
        self.abort_if_alert_doesnt_exist(id)

    def create(self, data):
        system = data
        system['id'] = self.counter = self.counter + 1
        self.systems.append(system)
        return system

    def update(self, id, data):
        system = self.get(id)
        system['name'] = data['name']
        return system

    def delete(self, id):
        system = self.get(id)
        self.systems.remove(system)
