import dropbox
from userdata_handler import *


class DropboxConnector:
    def __init__(self):
        self.userdata_handler = UserdataHandler()
        self.userdata = self.userdata_handler.load()
        self.access_token = self.userdata["access_token"]
        self.dropbox = None
        self.auth()
        self.access_token = None
        self.user_id = None

    def auth(self):
        self.dropbox = dropbox.Dropbox(self.access_token)

    def upload(self, filename):
        print(self.dropbox.upload)