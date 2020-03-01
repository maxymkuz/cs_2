import sys
from notebook import Note, Notebook


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        """ Creates an list of options"""
        self.notebook = Notebook()
        self.dict_of_choices = {"1": self.show_notes, "2": self.search_notes,
                                "3": self.add_note, "4": self.modify_note,
                                "5": self.quit}

    @staticmethod
    def display_menu():
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit""")

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.dict_of_choices.get(choice)
            print()
            if action:
                action()
            else:
                print(f"Sorry, {choice} is not a valid choice")

    def show_notes(self):
        if self.notebook.notes:
            for i in self.notebook.notes:
                print(i)
        else:
            print("There aren't any notes yet, create one first")

    def add_note(self):
        memo = input("Enter Memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def search_notes(self):
        filter = input("Enter the filter, you are looking for: ")
        print('\n'.join([i.__str__() for i in self.notebook.notes
                         if i.match(filter)]))

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a new memo: ")
        tags = input("Enter new tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
