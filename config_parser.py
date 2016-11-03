import json
import os


class ConfigParser:
    def __init__(self):
        dirname = os.path.dirname(os.path.realpath(__file__))
        print(os.path.join(dirname, "config.json"))
        self.filename = os.path.join(dirname, "config.json")
        self.directories_to_backup = None
        self.gdrive_bin = None
        self.json_file = None
        self.gdrive_dir_id = None
        self.parse_file()

    def read_file(self):
        with open(self.filename, "r") as f:
            self.json_file = json.loads(f.read())

    def parse_file(self):
        self.read_file()
        self.directories_to_backup = self.get_dirs_from_file()
        self.gdrive_bin = self.get_gdrive_bin()
        self.gdrive_dir_id = self.get_gdrive_dir_id()

    def get_dirs_from_file(self):
        dir_array = self.json_file["directories_to_backup"]
        for element in dir_array:
            if not os.path.exists(element):
                dir_array.remove(element)
        return dir_array

    def get_gdrive_bin(self):
        return self.json_file["gdrive_bin"]

    def get_gdrive_dir_id(self):
        return self.json_file["gdrive_dir_id"]

    def get_clean_time(self):
        return self.json_file["clean_time"]

