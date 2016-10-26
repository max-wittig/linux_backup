from quickstart import *
import os


class DriveConnector:
    def __init__(self):
        self.gdrive_location = "gdrive-linux-x64"
        self.folder_id = "0BxzwX_i76rPESm1USlhweGwtMWs"

    def upload(self, filename):
        os.system("./"+self.gdrive_location + " upload --parent " + self.folder_id + " " + filename)
