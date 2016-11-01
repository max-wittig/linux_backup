from drive_connector import *
from zip_creator import *
from config_parser import *
import time
import json


class LinuxBackup:
    def __init__(self):
        self.config_parser = ConfigParser()
        self.out_dir = os.path.join(os.path.dirname(__file__), "backups/")
        self.create_empty_dir()
        self.backup_name = "%s-%s.zip" % (os.getlogin(), time.strftime("%d-%m-%Y"))
        self.directorys = self.config_parser.directories_to_backup
        self.path = os.path.join(self.out_dir, self.backup_name)
        self.zip_creator = ZipCreator(self.path, self.directorys)
        self.drive_connector = DriveConnector(self.out_dir, self.config_parser)

    def create_empty_dir(self):
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def backup(self):
        self.zip_creator.create()
        self.drive_connector.upload(self.path)