class Character:
    """ Represents a single character in a document
    """
    def __init__(self, character, bold=False, italic=False, underline=False):
        """ Initializes a character and checks if it has
        additional properties"""
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
        """ Inserts an character in the given cursor position"""
        self.characters.insert(self.cursor.pos, character)

    def delete(self):
        """ Deletes a symbol in a given position
        """
        if len(self.characters) > self.cursor.pos:
            del self.characters[self.cursor.pos]
        else:
            print("There is nothing to delete as you are in the last element")

    def save(self, path):
        """ Saves given document to a .txt file
        >>> Document.save('document')
        None
        Saves the document contents into the file document.txt
        If user gives inappropriate location, prints a warning:"""
        self.filename = path
        if isinstance(self.filename, str) and self.filename:
            with open(self.filename + ".txt", 'w') as file:
                file.write("".join([str(char) for char in self.characters]))
        else:
            print("You have entered the wrong location, please retype it!")

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
        """ Moves the cursor one element forward"""
        if self.pos == len(self.document.characters):
            print("You are at the end of the file and your ")
        else:
            self.pos += 1
        print("Current cursor position: " + str(self.pos))

    def back(self):
        """ Moves the cursor one element back"""
        if self.pos == 0:
            print("There is no way back as the")
        else:
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
    doc = Document()
    cursor = Cursor(doc)

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
    cursor.forward()
    cursor.back()
    doc.delete()
    doc.insert(y)
    print(doc.string)

    doc.save("document")
