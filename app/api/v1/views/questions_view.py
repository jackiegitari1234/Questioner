#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v1 import vers1 as v1
from app.api.v1.models.questions_model import quiz,questions


@v1.route('/meetup/<int:id>/question', methods=['POST'])
def add_question(id,user=1):

    question_data = request.get_json()

    if not question_data:
        abort(make_response(jsonify({"message":"Only input of Application/JSON expected"}),400))
    
    # Check for empty inputs
    if not all(field in question_data for field in ["title","question"]):
        abort(make_response(jsonify({"message":"Please enter a question and it's title"}),400))

    if len (question_data) > 2:
        abort(make_response(jsonify({"message":"Please provide just the required fields"}),400))
    
    title = question_data ['title']
    questn = question_data ['question']

    
    Qstn = quiz(title,questn,user,id).add_Question()
    abort(make_response(jsonify({"data":Qstn}),201))

@v1.route('/questions/<int:id>/upvote', endpoint='upvote',methods=['PATCH'])
@v1.route('/questions/<int:id>/downvote', endpoint='downvote', methods=['PATCH'])
def votes(id):
    if request.endpoint == 'apiv1.upvote':
        Quizn = quiz().upvotes(id,user=1)
        abort(make_response(jsonify({"data":Quizn}),201))
    elif request.endpoint == 'apiv1.downvote':
        Quizn = quiz().downvotes(id,user=1)
        abort(make_response(jsonify({"data":Quizn}),201)) 


