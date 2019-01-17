questions = []
total_votes = []
total_downvotes = []
class quiz(object):    
    def __init__(self, title=None, question=None, user=None, meetup=None, votes=0):
        self.questionId = len(questions)+1
        self.user = user
        self.meetup = meetup
        self.title = title
        self.question = question
        self.votes = votes

    def add_Question(self):
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

    def upvotes(self,id,user):

        upvote_quiz = {
            "voter": user,
            "question": id
            }

        for vot in total_votes:
            #user has voted so remove the vote
            if vot['voter'] == user:
                total_votes.remove(upvote_quiz)
                for qtn in questions:
                    if qtn['id'] == id:
                        qtn['votes'] = qtn['votes'] -1
                        return qtn

        #user not voted, so add a vote
        total_votes.append(upvote_quiz)
        for qtn in questions:
            if qtn['id'] == id:
                qtn['votes'] = qtn['votes'] +1
                return qtn



    def downvotes(self,id,user):
        upvote_quiz = {
            "voter": user,
            "question": id
            }

        for vot in total_downvotes:
            #user has downvoted so remove the downvote
            if vot['voter'] == user:
                total_downvotes.remove(upvote_quiz)
                for qtn in questions:
                    if qtn['id'] == id:
                        qtn['votes'] = qtn['votes'] +1
                        return qtn

        #user can downvote
        total_downvotes.append(upvote_quiz)
        for qtn in questions:
            if qtn['id'] == id:
                qtn['votes'] = qtn['votes'] -1
                return qtn
                