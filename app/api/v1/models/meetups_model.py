meetups = []
class meetup(object):    
    def __init__(self, topic=None, location=None, happeningOn=None, tags=None):
        self.meetupId = len(meetups)+1
        self.topic = topic
        self.location = location
        self.happeningOn = happeningOn
        self.tags = tags

    def addMeetup(self):
        meetup = {
            "topic": self.topic,
            "location":self.location,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }
        return meetup