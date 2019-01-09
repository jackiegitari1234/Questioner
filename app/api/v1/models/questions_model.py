questions = []
class quiz(object):    
    def __init__(self, title=None, question=None, user=None, meetup=None):
        self.questionId = len(questions)+1
        self.user = user
        self.meetup = meetup
        self.title = title
        self.question = question

    def addQuestion(self):
        Question = {
            "user": self.user,
            "meetup":self.meetup,
            "title":self.title,
            "body":self.question
        }
        return Question