import shutil
import zipfile


class ZipProcessor:
    """ The class which helps helps to manipulate with zip files.
    You can unzip and replace stuff in .txt files or
    change the resolution of all files in all images"""

    def __init__(self, other):
        """ Initializes and makes path and directory"""
        self.other = other
        self.zip_name = other.filename
        self.temp_directory = other.temp_directory

    def process_zip(self):
        """ Simply calls all functions that do their work"""
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """ Unzips all files in the
        temporary directory"""
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zip_name) as zip:
            zip.extractall(str(self.temp_directory))

    def process_files(self):
        """ Uses the function from other class
        that is inputed"""
        self.other.process_files()

    def zip_files(self):
        """
        Compresses files and overwrites them into
        previous directory
        """
        with zipfile.ZipFile(self.zip_name, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
