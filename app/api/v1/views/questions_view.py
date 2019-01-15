#downloaded modules
from flask import jsonify,request

#local imports
from app.api.v1 import vers1 as v1
from app.api.v1.models.questions_model import quiz,questions


@v1.route('/meetup/<int:id>/question', methods=['POST'])
def add_question(id,user=1):

    question_data = request.get_json()

    if not question_data:
        return jsonify({"status": 400, "message": "Only input of Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in question_data for field in ["meetup_id","title","question"]):
        return jsonify({"status": 400, "message": "Please enter a question and it's title"})

    title = question_data ['title']
    questn = question_data ['question']

    
    Qstn = quiz(title,questn,user,id).addQuestion()
    return jsonify({"status": 201, "data": Qstn})

@v1.route('/questions/<int:id>/upvote', endpoint='upvote',methods=['PUT'])
@v1.route('/questions/<int:id>/downvote', endpoint='downvote', methods=['PUT'])
def votes(id):
    if request.endpoint == 'apiv1.upvote':
        Quizn = quiz().upvotes(id)
        return jsonify({"status": 201, "data": Quizn})
    elif request.endpoint == 'apiv1.downvote':
        Quizn = quiz().downvotes(id)
        return jsonify({"status": 201, "data": Quizn})


