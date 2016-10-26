from drive_connector import *
from zip_creator import *
import time


class LinuxBackup:
    def __init__(self):
        self.out_dir = "backups/"
        self.directorys_file_name = "directories_to_backup.txt"
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        self.backup_name = "%s-%s.zip" % (os.getlogin(), time.strftime("%d-%m-%Y"))
        self.directorys = self.get_dirs_from_file()
        self.path = os.path.join(self.out_dir, self.backup_name)
        self.zip_creator = ZipCreator(self.path, self.directorys)
        self.drive_connector = DriveConnector()

    def backup(self):
        self.zip_creator.create()
        self.drive_connector.upload(self.path)

    def get_dirs_from_file(self):
        with open(self.directorys_file_name, "r") as f:
            dir_string = f.read()
        dir_array = dir_string.split(";")
        for element in dir_array:
            if not os.path.exists(element):
                dir_array.remove(element)
        return dir_array
