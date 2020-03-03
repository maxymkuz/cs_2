import sys
from notebook import Note, Notebook


class Menu:
    """ Displays a command line menu and respond to choices from
     a user when runs."""

    def __init__(self):
        """ Creates an list of options"""
        self.notebook = Notebook()
        self.dict_of_choices = {"1": self.show_notes, "2": self.search_notes,
                                "3": self.add_note, "4": self.modify_note,
                                "5": self.quit}

    @staticmethod
    def display_menu():
        """ List a list of choices to a user"""
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit""")

    def run(self):
        """ (Menu) -> None
        Display the menu and respond to choices."""
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
        """ (Menu) -> None
        List a list of notes to a user"""
        if self.notebook.notes:
            for i in self.notebook.notes:
                print(i)
        else:
            print("There aren't any notes yet, create one first")

    def add_note(self):
        """ (Menu) -> None
        Inputs information and creates an note"""
        memo = input("Enter Memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def search_notes(self):
        """ (Menu) -> None
        Inputs filter and looks for it in notes"""
        filter = input("Enter the filter, you are looking for: ")
        print('\n'.join([i.__str__() for i in self.notebook.notes
                         if i.match(filter)]))

    def modify_note(self):
        """ (Menu) -> None
        Inputs information and modifies an note with a given ID"""
        id = input("Enter a note id: ")
        memo = input("Enter a new memo: ")
        tags = input("Enter new tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """ (Menu) -> None
        finishes the terminal session"""
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
