from machine import *
import unittest

class TestMachine(unittest.TestCase):
    def setUp(self) -> None:
        self.tm3 = TextMachine((25, 100), (25, 200))
        self.tm4 = TextMachine((25, 100), (25, 200))
        self.tm5 = TextMachine((20, 100), (15, 200))
        self.tm6 = TextMachine((25, 120), (25, 245))

    def test_equality(self):
        self.assertTrue(self.tm3 == self.tm4)
        self.assertTrue(self.tm3 != self.tm5)
        self.assertTrue(self.tm3 != self.tm6)
        self.assertTrue(self.tm3 != self.tm7)