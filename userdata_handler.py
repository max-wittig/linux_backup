import json


class UserdataSaver:
    def __init__(self, userdata):
        self.userdata = userdata

    def save(self)
        with open(self.userdata.service, "w") as f:
            f.write(json.dumps(self.userdata.to_object()))

    def load(self):
        pass
