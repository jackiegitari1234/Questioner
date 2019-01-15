questions = []
class quiz(object):    
    def __init__(self, title=None, question=None, user=None, meetup=None, votes=0):
        self.questionId = len(questions)+1
        self.user = user
        self.meetup = meetup
        self.title = title
        self.question = question
        self.votes = votes

    def addQuestion(self):
        Question = {
            "id" : self.questionId,
            "user": self.user,
            "meetup":self.meetup,
            "title":self.title,
            "body":self.question,
            "votes":self.votes
        }
        questions.append(Question)
        return Question

    def upvotes(self,id):
        for qtn in questions:
            if qtn['id'] == id:
                qtn['votes'] = qtn['votes'] +1
                return qtn
    def downvotes(self,id):
        for qtn in questions:
            if qtn['id'] == id:
                qtn['votes'] = qtn['votes'] -1
                return qtn
                