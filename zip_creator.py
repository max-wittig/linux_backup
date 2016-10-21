import zipfile
import os


class ZipCreator:
    def __init__(self, filename, directorys):
        self.filename = filename
        self.directorys = directorys

    """thx to https://www.calazan.com/how-to-zip-an-entire-directory-with-python/ for the code
    this is modified and simplified to handle multiple dirs
    """
    def zip_folder(self, folder_paths, output_path):
        zip_file = zipfile.ZipFile(self.filename, "w")
        for folder_path in folder_paths:
            print(folder_paths)
            parent_folder = os.path.dirname(folder_path)
            # Retrieve the paths of the folder contents.
            contents = os.walk(folder_path)
            try:
                for root, folders, files in contents:
                    # Include all subfolders, including empty ones.
                    for folder_name in folders:
                        absolute_path = os.path.join(root, folder_name)
                        relative_path = absolute_path.replace(parent_folder + '\\', '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)
                    for file_name in files:
                        absolute_path = os.path.join(root, file_name)
                        relative_path = absolute_path.replace(parent_folder + '\\', '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)
            except:
                print("Error")

        print("'%s' created successfully." % output_path)
        zip_file.close()

    def create(self):
        self.zip_folder(self.directorys, self.filename)
