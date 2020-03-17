from zip_replace import ZipReplace
from zip_processor import ZipProcessor
from scale_zip import ScaleZip
import os

replace = ZipReplace("1.zip", "search", "result")

for subdir, dirs, files in os.walk('./'):
    assert "1.zip" in files
    break

assert isinstance(replace, ZipReplace)
assert replace.search_string == "search"

z = ZipProcessor(replace)

assert isinstance(z, ZipProcessor)
assert "1.zip" == z.zip_name

scale = ScaleZip("images.zip", 100, 500)

assert isinstance(scale, ScaleZip)

for subdir, dirs, files in os.walk('./'):
    assert "images.zip" in files
    break

y = ZipProcessor(scale)

assert isinstance(y, ZipProcessor)
assert "images.zip" == y.zip_name
