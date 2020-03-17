from zip_processor import ZipProcessor
from scale_zip import ScaleZip

assert isinstance(ScaleZip("images.zip", '100', '100'), ScaleZip)
assert isinstance(ScaleZip("images.zip", '100', '100'), ZipProcessor)
assert ScaleZip("images.zip", '100', '100').temp_directory != \
       "unzipped-images"
assert ScaleZip("images.zip", '100', '100').height != 100
assert ScaleZip("images.zip", '100', '100').width != 100


print("Насправді тут дуже нема що ще тестувати, окрім витягувати "
      "розширення картинки і дивитись чи воно помінялось правильно.")
