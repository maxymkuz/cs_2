class CursorError(Exception):
    def __init__(self, position):
        self.position = position
        super().__init__(position)


class CursorBeforeFileError(CursorError):
    pass


class CursorAfterFileError(CursorError):
    pass


class DeleteNonexistentError(CursorError):
    pass


class NoNameSaveError(Exception):
    def __init__(self, filename):
        super().__init__(filename)


class WrongInputError(Exception):
    def __init__(self, ipt):
        super().__init__(ipt)
        self.input = ipt
