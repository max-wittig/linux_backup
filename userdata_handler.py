import json


class UserdataHandler:
    def __init__(self):
        self.debug = True
        if self.debug:
            self.filename = "app_secrets.json"
        else:
            self.filename = "app_secrets_release.json"

    def save(self, userdata):
        with open(self.filename, "w") as f:
            f.write(json.dumps(userdata.to_object()))

    def load(self):
        with open(self.filename, "r") as f:
            return json.loads(f.read())
