users = []


class User():

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
