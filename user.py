class User(object):
    """docstring for User"""
    def __init__(self, arg):
        super(User, self).__init__()
        self.arg = arg
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False

