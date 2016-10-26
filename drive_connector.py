import os


class DriveConnector:
    def __init__(self, out_dir, config_parser):
        self.out_dir = out_dir
        self.config_parser = config_parser
        self.gdrive_bin = self.config_parser.gdrive_bin
        self.gdrive_dir_id = self.config_parser.gdrive_dir_id

    def upload(self, filename):
        os.system(os.path.join("gdrive_bin", self.gdrive_bin)
                  + " upload --parent " + self.gdrive_dir_id + " " + filename)
