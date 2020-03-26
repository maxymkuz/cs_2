from document_exceptions import *


class Character:
    """ Represents a single character in a document
    """
    def __init__(self, character, bold=False, italic=False, underline=False):
        """ Initializes a character and checks if it has
        additional properties. RAISES AN ERROR IF THE INPUT IS NOT
        CORRECT"""
        if len(character) != 1:
            raise WrongInputError(character)
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """ Visual representation of a character"""
        bold = "|B:" if self.bold else ""
        italic = "|I:" if self.italic else ""
        underline = "|U:" if self.underline else ""
        return f"{bold}{italic}{underline}{self.character}"


class Document:
    """ Represents a single document which has
    cursor and a list of characters"""

    def __init__(self):
        """ Initializes a blank document"""
        self.characters = []
        self.cursor = None
        self.filename = ""

    def insert(self, character):
        """ Inserts an character in the given cursor position
        IF LENGTH OF THE INPUT IS NOR EQUAL TO 1, THE
        ERROR IS RAISED"""
        if not isinstance(character, str) and len(character.character) != 1:
            raise WrongInputError(character)
        self.characters.insert(self.cursor.pos, character)

    def delete(self):
        """ Deletes a symbol in a given position
        """
        if len(self.characters) > self.cursor.pos:
            del self.characters[self.cursor.pos]
        else:
            raise DeleteNonexistentError(self.cursor.pos)

    def save(self, path):
        """ Saves given document to a .txt file
        Document.save('document')
        Saves the document contents into the file document.txt
        If user gives inappropriate location, raises
        an exception!"""
        self.filename = path

        if not isinstance(self.filename, str) or not self.filename:
            raise NoNameSaveError(self.filename)
        with open(self.filename + ".txt", 'w') as file:
            file.write("".join([str(char) for char in self.characters]))


    @property
    def string(self):
        """ Property that prints all the characters
        from this document in a good way"""
        return "".join([str(char) for char in self.characters])


class Cursor:
    """ Represents a position in a list of characters
    in a document"""

    def __init__(self, document):
        self.pos = 0
        self.document = document
        self.document.cursor = self

    def forward(self):
        """ Moves the cursor one element forward. IF IT ALREADY
        IS THE END OF THE FILE, THEN THE ERROR IS RAISED"""
        if self.pos == len(self.document.characters):
            raise CursorAfterFileError(self.pos)
        self.pos += 1
        print("Current cursor position: " + str(self.pos))

    def back(self):
        """ Moves the cursor one element back. IF IT ALREADY
        IS THE BEGINNING, THEN THE ERROR IS RAISED"""
        if self.pos == 0:
            raise CursorBeforeFileError(self.pos)
        self.pos -= 1
        print("Current cursor position: " + str(self.pos))

    def home(self):
        """ Moves the cursor to the beginning of the document"""
        self.pos = 0
        print("Current cursor position: " + str(self.pos))

    def end(self):
        """ Moves the cursor to the end of the document"""
        self.pos = self.document.characters.__len__()
        print("Current cursor position: " + str(self.pos))


if __name__ == '__main__':
    # You can uncomment the errors which I made myself
    # If you want to see how exceptions work in this case
    try:
        doc = Document()
        cursor = Cursor(doc)
        # wrong_character = Character('xy')
        # cursor.forward()
        # doc.delete()
        # doc.save(123456)

        m = Character('m', bold=True)
        a = Character('a')
        x = Character('x', underline=True)
        y = Character('y')

        doc.insert(m)
        cursor.forward()
        doc.insert(a)
        doc.insert(a)
        cursor.forward()
        cursor.forward()
        doc.insert(x)
        cursor.end()
        doc.insert(x)
        cursor.end()
        cursor.back()
        doc.delete()
        print(doc.string)
        doc.save("document")

    except CursorBeforeFileError:
        print("You tried to go back to non-existent element")

    except CursorAfterFileError:
        print("You tried to go forward to non-existent element")

    except DeleteNonexistentError:
        print("You tried to delete a non-existent element")

    except NoNameSaveError:
        print("You tried to save a document into a notebook"
              " with an inappropriate name")

    except WrongInputError:
        print("You have to input a character, whose length is not than 1!!")
