'''THIS IS THE GLUE'''

#downloaded modules
from flask import Flask

# local imports
from Instance.config import app_config
from app.api.v1.views.meetups_view import v1 as V1_meetups
from app.api.v1.views.questions_view import v1 as V1_questions
from app.api.v1.views.auth_view import v1 as V1_auth

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(app_config["development"])
    app.register_blueprint(V1_questions)
    app.register_blueprint(V1_questions)
    app.register_blueprint(V1_auth)
    # app.config["SECRET_KEY"] = "hsgghcguyds"
    return app


