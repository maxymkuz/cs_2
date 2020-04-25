from arrays import Array2D


class GrayscaleImage:
    """
    Represents an image
    """
    def __init__(self, nrows, ncols):
        self._rows = nrows
        self._cols = ncols
        self._image = Array2D(nrows, ncols)
        # Set all the values to 0
        self.clear(0)

    def clear(self, value):
        """
        clears the  array
        """
        if not isinstance(value, int):
            raise ValueError("Not integer")
        if not (0 <= value <= 255):
            raise ValueError('Between 0 and 255')
        self._image.clear(value)

    def height(self):
        """
        Returns a height of an image
        """
        return self._rows

    def width(self):
        """
        Returns a width of an image
        """
        return self._cols

    def getitem(self, row, col):
        """
        Returns the value in a given cell
        """
        return self._image[row, col]

    def setitem(self, row, col, value):
        """
        Sets the value to a row and col if valid, else raise exception
        """
        if not isinstance(value, int):
            raise ValueError("Not integer")
        if not (0 <= value <= 255):
            raise ValueError('Between 0 and 255')
        if not (0 <= row < self._rows) or not (0 <= col < self._cols):
            raise ValueError("Wrong index")
        self._image[row, col] = value


if __name__ == '__main__':
    img = GrayscaleImage(10, 10)
    for i in range(10):
        for j in range(10):
            img.setitem(i, j, i + j)
    img.setitem(10, 9, 33)

