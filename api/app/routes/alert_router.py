from utils.http_response_codes import HTTPStatus
from flask_restplus import Resource, Namespace
from serializers.alert_serializers import alert_model_input as input, alert_model as output

ns = Namespace('alert', description='Alerting system')

class AlertRouter:
    def __init__(route, AbstractController):
        route.alert_ctrl = AbstractController
        alert_model_input = ns.model('alert_model_input', input)
        alert_model = ns.model('alert_model', output)

        @ns.route('/', methods=['POST', 'GET'])
        class AlertList(Resource):
            '''Shows a list of all alerts, and lets you POST to add new alerts'''
            @ns.doc('list_alerts')
            @ns.marshal_list_with(alert_model)
            def get(alert_list):
                '''List all alerts'''
                return route.alert_ctrl.get_all()

            @ns.doc('create_alert')
            @ns.expect(alert_model_input, mask='name')
            @ns.marshal_with(alert_model, code=HTTPStatus.CREATED)
            def post(alert_list):
                '''Create a new alert'''
                args = ns.payload
                print('\nargs:',args,'\n')
                alert = route.alert_ctrl.create(args)
                print(alert)
                return alert, HTTPStatus.CREATED

        @ns.route('/<int:id>', methods=['DELETE','GET', 'PUT'])
        @ns.response( HTTPStatus.NOT_FOUND, 'Alert not found')
        @ns.param('id', 'The alert identifier')
        class Alert(Resource):
            '''Show a single alert item and lets you delete them'''
            @ns.doc('get_todo')
            @ns.marshal_with(alert_model)
            def get(alert_item, id):
                '''Fetch a alert given its identifier'''
                return route.alert_ctrl.get(id)

            @ns.doc('delete_alert')
            @ns.response(HTTPStatus.NO_CONTENT, 'Alert deleted')
            def delete(alert_item, id):
                '''Delete a alert given its identifier'''
                route.alert_ctrl.delete(id)
                return '', HTTPStatus.NO_CONTENT

            @ns.doc('put_alert')
            @ns.expect(alert_model)
            @ns.marshal_with(alert_model)
            def put(alert_item, id):
                '''Update a alert given its identifier'''
                args = ns.payload
                return route.alert_ctrl.update(id, args)
