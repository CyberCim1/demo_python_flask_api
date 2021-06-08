from flask_restplus import fields

alert_model_input = {
    'name': fields.String(required=True, description='The system that triggered the alert', min_length=1, max_length=40)
}

alert_model = {
    'id': fields.Integer(required=True, readOnly=True, description='The system unique identifier'),
    'name': fields.String(required=True, description='The system that triggered the alert', min_length=1, max_length=40)
}
