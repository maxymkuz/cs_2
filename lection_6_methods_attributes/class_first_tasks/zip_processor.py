import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """ The parent class of other classes.
    Helps to manipulate with zip files"""
    def __init__(self, zipname):
        """ Initializes and makes path and directory"""
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

    def process_zip(self):
        """ Simply calls all functions"""
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """ Unzips all files in the
        temporary directory"""
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        Compresses files and overwrites them into
        previous directory
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


class ZipReplace(ZipProcessor):
    """ An additional class that lets user to replace a given
    piece of text in all .txt files in the zip file"""
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """Perform a search and replace on all files in the
        temporary directory"""
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                content = file.read()
            content = content.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(content)
