import zipfile
import os


class ZipCreator:
    def __init__(self, filename, directorys):
        self.filename = filename
        self.out_dir = "backups"
        self.directorys = directorys
        self.zipfile = zipfile.ZipFile(self.filename, "w")

    """thx to https://www.calazan.com/how-to-zip-an-entire-directory-with-python/ for the code
    this is just slightly modified
    """
    def zip_folder(self, folder_paths, output_path):
        zip_file = zipfile.ZipFile(output_path, 'w')
        for folder_path in folder_paths:
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
                        print("'%s' created successfully." % output_path)
            except:
                print("Error")

        zip_file.close()

    def create(self):
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        path = os.path.join(self.out_dir, self.filename)
        self.zip_folder(self.directorys, path)
