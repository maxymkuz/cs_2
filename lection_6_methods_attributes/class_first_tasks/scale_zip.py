from zip_processor import ZipProcessor
import sys
from PIL import Image


class ScaleZip(ZipProcessor):
    """
    This class is used to change the resolution
    of all images in a given zip file
    """
    def __init__(self, filename, width, height):
        super().__init__(filename)
        self.width = width
        self.height = height

    def process_files(self):
        """Scale each image in the directory to
        a format, chosen by a user
        """
        try:
            for filename in self.temp_directory.iterdir():
                im = Image.open(str(filename))
                scaled = im.resize((int(self.height), int(self.width)))
                scaled.save(str(filename))
        except ValueError:
            print("You entered non integer values")


if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
