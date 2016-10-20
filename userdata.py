class UserData:
    def __init__(self, access_token, service):
        self.access_token = access_token
        self.service = service

    def to_object(self):
        json_object = {
            "access_token": self.access_token
        }
        return json_object
