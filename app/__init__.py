'''THIS IS THE GLUE'''

#downloaded modules
from flask import Flask, jsonify

# local imports
from Instance.config import app_config
from app.api.v1.views.meetups_view import v1 as V1_meetups
from app.api.v1.views.questions_view import v1 as V1_questions
from app.api.v1.views.auth_view import v1 as V1_auth

#edge
def invalid_method(error):
    return jsonify({
        'error': str(error),
        'status': 405
        }), 405

#bad request
def bad_request(error):
    return jsonify({
        'error': str(error),
        'status': 400
        }), 400

#unexisting url
def page_not_found(error):
    return jsonify({
        'error': str(error),
        'status': 404
        }), 404

#internal server error
def server_error(error):
    return jsonify({
        'error': str(error),
        'status': 500
        }), 500



def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(app_config["development"])
    app.register_blueprint(V1_questions)
    app.register_blueprint(V1_questions)
    app.register_blueprint(V1_auth)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(400, bad_request)

    # app.config["SECRET_KEY"] = "hsgghcguyds"
    return app


