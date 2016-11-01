import os


class DriveConnector:
    def __init__(self, out_dir, config_parser):
        self.out_dir = out_dir
        self.config_parser = config_parser
        self.gdrive_bin = self.config_parser.gdrive_bin
        self.gdrive_dir_id = self.config_parser.gdrive_dir_id

    def upload(self, filename):
        dirname = os.path.dirname(os.path.realpath(__file__))
        os.system(os.path.join(dirname, "gdrive_bin", self.gdrive_bin)
                  + " upload --parent " + self.gdrive_dir_id + " " + filename)
