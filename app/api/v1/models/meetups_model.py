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
            "id" : self.meetupId,
            "topic": self.topic,
            "location":self.location,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }
        meetups.append(meetup)
        return meetup
    def upvotes(self,id):
        for meetup in meetups:
            if meetup['id'] == id:
                return meetup



RSVPs = []
class rsvp(object):
    def __init__(self, meetup=None, user=None, response=None):
        self.rsvpId = len(RSVPs)+1
        self.user = user
        self.response = response
        self.meetup = meetup

    def addRsvp(self):
        rsvp = {
            "id" : self.rsvpId,
            "user": self.user,
            "response":self.response,
            "meetup":self.meetup
        }
        RSVPs.append(rsvp)
        return rsvp
