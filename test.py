class Chapter:
    def __init__(self, name, pages):
        self.title = name
        self.pages = pages


class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters
        self.__max = "max"

    @property
    def chapterCount(self):
        return len(self.chapters)

    def getPageCount(self):
        return sum([a.pages for a in self.chapters])

    def getChapter(self, num):
        return self.chapters[num]

    def moveChapter(self, num, other):
        other.chapters.append(self.getChapter(num))
        self.chapters = self.chapters[:num] + self.chapters[num + 1:]


chapterA = Chapter('I love CS!', 30)  # chapter title, # of pages
chapterB = Chapter('So do I!', 15)
book1 = Book('CS is Fun!', [chapterA, chapterB])  # book title, chapters
book2 = Book('The Short Book', [Chapter('Quick Read!', 5)])

print(book1._Book__max)

assert (book1.chapterCount == 2)
assert (book1.getPageCount() == 45)
assert (book2.chapterCount == 1)
assert (book2.getPageCount() == 5)
assert (book1.getChapter(0).title == 'I love CS!')
assert (book1.getChapter(1).title == 'So do I!')
assert (book2.getChapter(0).title == 'Quick Read!')
# Move chapter 0 from book1 to the end of book2
# so moveChapter always moves to the end of the target book.
book1.moveChapter(0, book2)
assert (book1.chapterCount == 1)
assert (book1.getPageCount() == 15)
assert (book1.getChapter(0).title == 'So do I!')
assert (book2.chapterCount == 2)
assert (book2.getPageCount() == 35)
assert (book2.getChapter(0).title == 'Quick Read!')
assert (book2.getChapter(1).title == 'I love CS!')
