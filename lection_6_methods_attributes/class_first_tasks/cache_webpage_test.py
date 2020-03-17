import cache_webpage
import time

if __name__ == '__main__':
    w = cache_webpage.WebPage(
        'https://gist.githubusercontent.com/maxymkuz/596220478ee8b1f7954dc4c1'
        'a2ce9c36/raw/6962aecd8e8651187b29cd3fd2540e2961eb1e2e/'
        'cache_webpage_test.txt')
    # We are retrieving a new content into cache
    print(w.content)
    assert isinstance(w, cache_webpage.AbstractWebPage)
    assert isinstance(w, cache_webpage.WebPage)
    assert w.content == b'cache webpage test'

    time.sleep(1)
    print("\nAbout one second passed from last update, so we "
          "do not retrieve it now:\n")
    print(w.content)

    time.sleep(9)
    print("\nMore than 10 seconds passed since last update, so we "
          "retrieve it now:\n")
    print(w.content)
