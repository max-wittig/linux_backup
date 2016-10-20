from dropbox_connector import *
from zip_creator import *
import time


class LinuxBackup:
    def __init__(self):
        self.backup_name = "home-%s.zip" % (time.strftime("%d-%m-%Y"))
        print(self.backup_name)
        self.directorys = ["/home/max/Desktop/", "/home/max/deadspaghetti/"]
        self.zip_creator = ZipCreator(self.backup_name, self.directorys)
        self.dropbox_connector = DropboxConnector()

    def backup(self):
        self.zip_creator.create()
        #self.dropbox_connector.upload(self.backup_name)