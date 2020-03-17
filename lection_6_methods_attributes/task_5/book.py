class Book:
    """ Represents a book. A Book has a title, and author, and a number of
    pages. It also has a current page, which always starts at 1. There is
    no page 0!"""

    def __init__(self, name, author, num_of_pages):
        """ Initializes an instance of book"""
        self.name = name
        self.author = author
        self.num_of_pages = num_of_pages
        self.current_page = 1
        self.bookmarked_page = None

    def turnPage(self, pages):
        """ Turns a page forward or backwards"""
        self.current_page += pages
        if self.current_page < 1:
            self.current_page = 1
        elif self.current_page > self.num_of_pages:
            self.current_page = self.num_of_pages

    def getCurrentPage(self):
        return self.current_page

    def placeBookmark(self):
        """ Places bookmark on the current page"""
        self.bookmarked_page = self.current_page

    def getBookmarkedPage(self):
        """ Returns None if not bookmarked yet"""
        return self.bookmarked_page

    def turnToBookmark(self):
        """ Redirects user to bookmarked page"""
        if self.bookmarked_page:
            self.current_page = self.bookmarked_page

    def removeBookmark(self):
        self.bookmarked_page = None

    def __eq__(self, other):
        """ Compares two books witha ll parameters and return bool"""
        if self.name == other.name and self.author == other.author and \
                self.num_of_pages == other.num_of_pages and \
                self.current_page == other.current_page and \
                self.bookmarked_page == other.bookmarked_page:
            # print(self, other)
            return True
        return False

    def __str__(self):
        """ Textual representation"""
        page = "page" if self.num_of_pages == 1 else "pages"
        bookmark = ", page 10 bookmarked" if self.bookmarked_page else ""
        return f"Book<{self.name} by {self.author}: {self.num_of_pages} " \
               f"{page}, currently on page {self.current_page}{bookmark}>"
