class find_item(object):
    def __init__(self, user_data=None,title=None,body=None):
        self.user_data = user_data
        self.title = title
        self.body = body

    def item(self):
        if not all(field in self.user_data for field in [self.title,self.body]):
            return False
        