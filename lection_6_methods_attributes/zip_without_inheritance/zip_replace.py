from pathlib import Path
import sys
from zip_processor import ZipProcessor


class ZipReplace:
    """ A class that lets user to replace a given
    piece of text in all .txt files in the zip file"""
    def __init__(self, filename, search_string, replace_string):
        """ Initializes an instance of this class"""
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped-{self.filename[:-4]}")

    def process_files(self):
        """ Performs a search and replace on all files in the
        temporary directory"""
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                content = file.read()
            content = content.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(content)


if __name__ == '__main__':
    replace = ZipReplace(*sys.argv[1:4])
    ZipProcessor(replace).process_zip()
