import os
import time


class Cleaner:
    def __init__(self, path, clean_time):
        self.path = path
        self.clean_time = clean_time

    def clean(self):
        self.clean_file_system()
        self.clean_drive()

    def clean_file_system(self):
        i = 0
        for filename in os.listdir(self.path):
            file = os.path.join(self.path, filename)
            creation_time = int(os.path.getctime(file))
            current_time = int(time.time())
            if current_time - creation_time > self.clean_time:
                os.remove(file)
                i += 1
        print(str(i) + " old files cleaned")

    def clean_drive(self):
        pass