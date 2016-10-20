class UserData:
    def __init__(self, username, password, service):
        self.username = username
        self.service = service
        self.password = password

    def to_object(self):
        json_object = {
            "username": self.username,
            "password": self.password
        }
        return json_object
