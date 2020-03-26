import auth
import sys
from notebook import Note, Notebook

# make all possible permissions
auth.authorizor.add_permission("Show all Notes")
auth.authorizor.add_permission("Show user's Notes")
auth.authorizor.add_permission("Search Notes")
auth.authorizor.add_permission("Add Note")
auth.authorizor.add_permission("Modify Note")

# set admin user
auth.authenticator.add_user("Admin", "qwerty123")

# set all possible rights of admin
auth.authorizor.permit_user("Show all Notes", "Admin")
auth.authorizor.permit_user("Show user's Notes", "Admin")
auth.authorizor.permit_user("Search Notes", "Admin")
auth.authorizor.permit_user("Add Note", "Admin")
auth.authorizor.permit_user("Modify Note", "Admin")

admin_notebook = Notebook()

# set an instance of default user
auth.authenticator.add_user("usual_user", "password123")

# set permission of default user
auth.authorizor.permit_user("Add Note", "usual_user")
auth.authorizor.permit_user("Show user's Notes", "usual_user")
auth.authorizor.permit_user("Search Notes", "usual_user")
auth.authorizor.permit_user("Modify Note", "usual_user")

default_user_notebook = Notebook()

notebooks_dict = {"Admin": admin_notebook, "user": default_user_notebook}


class Editor:
    def __init__(self):
        self.username = None
        self.notebook = None
        self.menu_map = {
            '1': self.login,
            '2': self.show_notes,
            '3': self.search_notes,
            '4': self.add_note,
            '5': self.modify_note,
            '6': self.show_all_notes,
            '7': self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
                self.notebook = notebooks_dict[username]

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def show_notes(self, notes=None):
        """Shows all the notes from the notebook of current user"""
        if self.is_permitted("Show user's Notes"):
            if notes is None:
                notes = self.notebook.notes
            for note in notes:
                print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def show_all_notes(self):
        if self.is_permitted("Show all Notes"):
            for user in notebooks_dict:
                print("Notes of " + user + ":")
                for note in notebooks_dict[user].notes:
                    print(
                        "{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        """Searches a particular note from the notebook"""
        if self.is_permitted("Search Notes"):
            filter = input("Search for: ")
            notes = self.notebook.search(filter)
            self.show_notes(notes)

    def add_note(self):
        """Adds a note to a notebook"""
        if self.is_permitted("Add Note"):
            memo = input("Enter a memo: ")
            self.notebook.new_note(memo)
            print("Your note has been added.")

    def modify_note(self):
        """Modifies a particular note in a notebook"""
        if self.is_permitted("Modify Note"):
            id = input("Enter a note id: ")
            memo = input("Enter a new memo: ")
            tags = input("Enter new tags: ")
            if memo:
                self.notebook.modify_memo(id, memo)
            if tags:
                self.notebook.modify_tags(id, tags)

    @staticmethod
    def quit():
        """Quits the Notebook menu"""
        print("Thank you for using your notebook today.")
        sys.exit(0)

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
    Notebook Menu
    1. Login
    2. Show user's Notes
    3. Search Notes
    4. Add Note
    5. Modify Note
    6. Show notes of every user
    7. Quit
    """
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()
