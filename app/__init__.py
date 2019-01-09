'''THIS IS THE GLUE'''

from flask import Flask

create_app = Flask(__name__)
create_app.config['SECRET_KEY'] = "thhjsbahjbhcdahbdshbhalhbhdhjdcbhs"

# local import
from app.api.v1.views.meetups_view import v1 as V1_meetups
from app.api.v1.views.questions_view import v1 as V1_questions

create_app.register_blueprint(V1_questions)
create_app.register_blueprint(V1_questions)