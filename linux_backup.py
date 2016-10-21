from dropbox_connector import *
from zip_creator import *
import time


class LinuxBackup:
    def __init__(self):
        self.out_dir = "backups/"
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        self.backup_name = "home-%s.zip" % (time.strftime("%d-%m-%Y"))
        self.directorys = ["/home/max/Documents/Travel/", "/home/max/Pictures/"]
        self.path = os.path.join(self.out_dir, self.backup_name)
        self.zip_creator = ZipCreator(self.path, self.directorys)
        self.dropbox_connector = DropboxConnector()

    def backup(self):
        self.zip_creator.create()
        self.dropbox_connector.upload(self.path)
