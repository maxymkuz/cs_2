from grayscaleimage import GrayscaleImage
from random import randint


def compress(img):
    """
    This function should compress an Gray scale image.
    TODO finish this function up in the future
    """
    raise NotImplementedError


if __name__ == '__main__':
    img = GrayscaleImage(10, 10)
    for i in range(10):
        for j in range(10):
            img.setitem(i, j, randint(0, 255))
    for i in range(10):
        print()
        for j in range(10):
            print(img.getitem(i, j), end=' ')
    # Should return an error:
    # img.setitem(10, 9, 33)
