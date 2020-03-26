def combine_character(plain, keyword):
    """(str, str) -> str
    Returns a char based on Vigenere cypher keyword
    used in encoding
    """
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    """(str, str) -> str
    Returns a char based on Vigenere cypher keyword
    used in decoding
    """
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)


class VigenereCipher:
    def __init__(self, keyword):
        """
        The main class. You can both encode and decode
        any message based on the keyword, you enter. If you
        want to decode an message with spaces, it will eliminate
        them. Do not use it with not-English and non-alphabetical
        symbols!
        """
        self.keyword = keyword

    def extend_keyword(self, number):
        """
        If the message is longer than the keyboard,
        repeat keyword several times
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        """
        Main function used to both encode and decode
        based on which two function you input into them
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plaintext):
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        return self._code(ciphertext, separate_character)