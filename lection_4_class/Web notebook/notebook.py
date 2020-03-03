import datetime

note_id = 1


class Note:
    """ Represent a note in the notebook"""

    def __init__(self, memo, creation_date, tags=''):
        """initialize a note with memo and optional
        space-separated tags."""
        self.memo = memo
        self.tags = tags if len(tags) > 1 else 'None'
        self.creation_date = creation_date
        global note_id
        self.id = note_id
        note_id += 1

    def modify(self, new_memo, new_tags):
        """ (Note, str) -> None
        Modifies an Note"""
        self.memo, self.tags = new_memo, new_tags

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise."""
        return filter.lower() in self.memo.lower() or \
               filter.lower() in self.tags.lower()

    def __str__(self):
        """ Prints an object"""
        return '\n'.join([f"{self.memo}. TAGS: {self.tags}"
                          f"          CREATION DATE: {self.creation_date}"])


class Notebook:
    """Represent a collection of notes that can be tagged and searched      """

    def __init__(self, notes=[]):
        self.notes = notes
    
    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def new_note(self, memo, tags='None'):
        """ Adds a new note"""
        self.notes.append(Note(memo, datetime.date.today(), tags))

    def modify_memo(self, id, memo):
        """ Modifies the memo"""
        if self._find_note(id):
            self._find_note(id).modify(memo, self._find_note(id).tags)
            print("Your note has been successfully modified")

    def modify_tags(self, id, tags):
        """ Modifies the tags"""
        if self._find_note(id):
            self._find_note(id).modify(self._find_note(id).memo, tags)
            print("Your note has been successfully modified")

    def search(self, filter):
        """Find all notes that match the given filter"""
        return [i for i in self.notes if i.match(filter)]

    def delete_note(self, note_id):
        if self._find_note(id):
            self.notes.remove(id)
            print("deleted successfully")
            # del self._find_note(id)


    # def __str__(self):
    #     return '\n'.join([f"{i.id}. {i.memo}. TAGS: {i.tags}  CREATION DATE: {i.creation_date}" for i in self.notes])
