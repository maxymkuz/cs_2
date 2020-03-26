from is_sorted import *
import unittest


class TestIsSorted(unittest.TestCase):
    def test_usual_case(self):
        lst_1 = [1, 2, 3, 4, 100]
        lst_2 = [100, 4, 3, 2, 1]
        lst_3 = [1, 2, 3, 4, 1]
        self.assertTrue(is_sorted(lst_1))
        self.assertFalse(is_sorted(lst_2))
        self.assertFalse(is_sorted(lst_3))

    def test_equal_elements(self):
        lst_4 = [2, 2, 2, 2, 2]
        lst_5 = [1, 2, 2, 2, 4]
        lst_6 = [3, 2, 2, 2, 4]
        self.assertTrue(is_sorted(lst_4))
        self.assertTrue(is_sorted(lst_5))
        self.assertFalse(is_sorted(lst_6))

    def test_tuple_input(self):
        tup_1 = (1, 2, 3, 4, 100)
        tup_2 = (1, 1, 1, 1, 1)
        tup_3 = (2, 1, 1, 1, 2)
        self.assertTrue(is_sorted(tup_1))
        self.assertTrue(is_sorted(tup_2))
        self.assertFalse(is_sorted(tup_3))

    def test_wrong_type_input(self):
        dict_1 = {"max": "Kuzyshyn", 1: 34}
        self.assertRaises(NotCorrectInputTypeError, is_sorted, dict_1)
        self.assertRaises(NotCorrectInputTypeError, is_sorted, 12234)
        self.assertRaises(NotCorrectInputTypeError, is_sorted, 12234.34536)
        self.assertRaises(NotCorrectInputTypeError, is_sorted, {1, 2, 3})

    def test_unhashable_inside_input(self):
        lst_2 = [4, 4, [100, 4, 2, 1], 2, 1]
        lst_3 = [1, 2, 3, 4, 100, [lst_2]]
        lst_4 = [{1, 2, 3, 4, 1}, 1, 2, 3, 4, 1]
        self.assertRaises(UnhashableElemInsideError, is_sorted, lst_2)
        self.assertRaises(UnhashableElemInsideError, is_sorted, lst_3)
        self.assertRaises(UnhashableElemInsideError, is_sorted, lst_4)

    def test_different_type_inside(self):
        lst_1 = [1, 2, 3, 4, 100, "1023"]
        lst_2 = [1, 2, 3, 4, 100, 1023.234535]
        self.assertRaises(IptWithDifferentElementsError, is_sorted, lst_1)
        self.assertRaises(IptWithDifferentElementsError, is_sorted, lst_2)


if __name__ == '__main__':
    unittest.main()
