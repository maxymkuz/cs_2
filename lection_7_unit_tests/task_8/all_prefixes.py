class NotASingleWordError(Exception):
    def __init__(self, ipt):
        self.ipt = ipt


class NotAStringError(Exception):
    def __init__(self, ipt):
        self.ipt = ipt


def all_prefixes(string):
    """
    This function reads the first letter of the word
    and returns a set of all prefixes of a given word,
    that start with a first letter
    If the input is not a string or other complication, raises
    different appropriate kinds of errors
    :param string: str
    :return: set
    """
    if not isinstance(string, str):
        raise NotAStringError(string)
    string = string.lower()
    if len(string.split()) != 1:
        raise NotASingleWordError(string)
    if len(string) >= 1:
        first_letter = string[0]
    res = []
    for i in range(len(string)):
        if string[i] == first_letter:
            res += [string[i:j+1] for j in range(i, len(string))]
            # print([string[i:j+1] for j in range(i, len(string))])
    return set(res)

# if __name__ == '__main__':
    # import unittest
    # print(help(unittest.TestCase.assertRaises))