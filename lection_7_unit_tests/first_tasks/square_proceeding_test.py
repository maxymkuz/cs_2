import unittest
from square_preceding import square_preceding


class TestPoint(unittest.TestCase):
    def test_edge_case(self):
        test_list = []
        square_preceding(test_list)
        self.assertEqual(test_list, [])

    def test_normal_cases(self):
        test_list = [1, 2, 3]
        square_preceding(test_list)
        self.assertEqual(test_list, [0, 1, 4])
        test_list = [0, 0, 0, 0]
        square_preceding(test_list)
        self.assertEqual(test_list, [0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()