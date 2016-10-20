import json


class UserdataHandler:
    def __init__(self):
        self.filename = "app_secrets.json"

    def save(self, userdata):
        with open(self.filename, "w") as f:
            f.write(json.dumps(userdata.to_object()))

    def load(self):
        with open(self.filename, "r") as f:
            return json.loads(f.read())
