from urllib.request import urlopen
import time


class AbstractWebPage:
    """ Is a parent for other WebPage"""
    def __init__(self, url):
        """ Initializes an incrance with url and
        the time when this content was last modified"""
        self.url = url
        self.last_modified = 0
        self._content = None

    @property
    def content(self):
        raise NotImplementedError


class WebPage(AbstractWebPage):
    """ This class will help to retrieve and
    return data from a url that is given"""
    TIME_DELTA = 10

    def __init__(self, url):
        """ (str) -> None
        Initializes an webpage"""
        super().__init__(url)
        self.last_modified = 0

    @property
    def content(self):
        """ () -> str
        Retriave a new webpage if it does not exist
        or last retrieve was more thaln TIME_DELTA sec ago
        else upload from cache"""
        if not self._content or time.time() - self.last_modified > WebPage.TIME_DELTA:
            print("Retrieving new version of this page...")
            self._content = urlopen(self.url).read()
            self.last_modified = time.time()
        return self._content
