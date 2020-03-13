class Position:
    """
    Represents a position with coordinates in board
    """
    def __init__(self, x, y, color):
        """
        Initialize with coordinates and color
        """
        self.y = y
        self.x = x
        self.color = color


class ChessSet:
    """ It's a set with chess Board + all other pieces"""
    def __init__(self, pieces, board):
        self.pieces = pieces
        self.board = board


class Board:
    """ Represents an chess Board and has all board positions inside"""
    def __init__(self, positions: list):
        """ Initializes object with list of all pieces and board"""
        self.position = positions


class Piece:
    """
    Represents a piece"""
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos


class Knight(Piece):
    """
    Represents a Knight and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)


class Bishop(Piece):
    """
    Represents a Bishop and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)


class Pawn(Piece):
    """
    Represents a Pawn and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)


class Hook(Piece):
    """
    Represents a Hook and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)


class Horse(Piece):
    """
    Represents a Hourse and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)


class Queen(Piece):
    """
    Represents a Queen and inherits from Piece"""
    def __init__(self, color, pos, shape):
        self.shape = shape
        super().__init__(color, pos)
