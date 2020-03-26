import unittest
from line import *


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.A = Point(5, 6)
        self.B = Point(6, 10)
        self.C = Point(5.0, 6.0)
        self.D = Point(-5, -6)

    def test_init(self):
        self.assertEqual((self.A.x, self.A.y),
                         (float(5), float(6)),
                         "Значения не дійсні числа!")
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)),
                         "Значения не дійсні числа!")
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)),
                         "Значения не дійсні числа!")
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)),
                         "Значения не дійсні числа!")

    def test_str(self):
        self.assertTrue(str(self.A) == "(5.0, 6.0)",
                        "Неправильний вивід на екран!")

        self.assertTrue(str(self.B) == "(6.0, 10.0)",
                        "Неправильний вивід на екран!")
        self.assertTrue(str(self.C) == "(5.0, 6.0)",
                        "Неправильний вивід на екран!")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)",
                        "Неправильний вивід на екран!")

    def test_eq(self):
        self.assertTrue(self.A == self.C,
                        "Дві однакові точки при тестуванні виявились не однаковими!")
        self.assertFalse(self.A == self.B,
                         "Дві різні точки при тестуванні виявилися однаковими!")
        self.assertFalse(self.A == self.D,
                         "Дві різні точки при тестуванні виявилися однаковими!!")

    def test_ne(self):
        self.assertFalse(self.A != self.C,
                         "Дві однакові точки при тестуванні виявились не однаковими!")

        self.assertTrue(self.A != self.B,
                        "Дві різні точки при тестуванні виявилися однаковими!")
        self.assertTrue(self.A != self.D,
                        "Дві різні точки при тестуванні виявилися однаковими!")

    def test_get_xposition(self):
        self.assertEqual(self.A.x, float(5),
                         "Значения x не дійсне число!")

        self.assertEqual(self.B.x, float(6), "Значения x не дійсне число!")
        self.assertEqual(self.C.x, float(5), "Значения x не дійсне число!")
        self.assertEqual(self.D.x, float(-5), "Значения x не дійсне число!")

    def test_get_yposition(self):
        self.assertEqual(self.A.y, float(6),
                         "Значения y не дійсне число!")

        self.assertEqual(self.B.y, float(10), "Значения y не дійсне число!")
        self.assertEqual(self.C.y, float(6), "Значения y не дійсне число!")
        self.assertEqual(self.D.y, float(-6), "Значения y не дійсне число!")


class TestLine(unittest.TestCase):
    def setUp(self):
        self.l1 = Line([Point(0, 0), Point(1, 1)])
        self.l2 = Line([Point(0, 1), Point(1, 2)])
        self.l3 = Line([Point(1, 3), Point(4, 3)])  # Horizontal line
        self.l4 = Line([Point(1, 1), Point(5, 5)])
        self.l5 = Line([Point(3, 1), Point(3, 5)])  # Vertical line
        self.l6 = Line([Point(3, 10), Point(3, 500)])  # Vertical line
        self.l7 = Line([Point(0, 10), Point(0, 500)])  # Vertical line

    def test_str(self):
        self.assertEqual(str(self.l1), "1.0 * x + 0.0 = y", "wrong init "
                                                            "method")
        self.assertEqual(str(self.l2), "1.0 * x + 1.0 = y", "wrong init "
                                                            "method")
        self.assertEqual(str(self.l3), "0.0 * x + 3.0 = y", "wrong init "
                                                            "method")
        self.assertEqual(str(self.l4), "1.0 * x + 0.0 = y", "wrong init "
                                                            "method")
        self.assertEqual(str(self.l5), "-1.0 * x + 3.0 = 0", "wrong init "
                                                             "method")
        self.assertEqual(str(self.l6), "-1.0 * x + 3.0 = 0", "wrong init "
                                                             "method")
        self.assertEqual(str(self.l7), "-1.0 * x + 0.0 = 0", "wrong init "
                                                             "method")

    def test_intersect_usual_case(self):
        self.assertAlmostEqual(self.l1.intersect(self.l2), False, 10,
                               "Computation error")
        self.assertEqual(self.l1.intersect(self.l3), Point(3, 3),
                         "Computation error")
        self.assertEqual(self.l1.intersect(self.l4), self.l1,
                         "Computation error")
        self.assertEqual(self.l3.intersect(self.l5), Point(3, 3),
                         "Computation error")
        self.assertEqual(self.l5.intersect(self.l4), Point(3, 3),
                         "Computation error")
        self.assertEqual(self.l4.intersect(self.l2), False,
                         "Computation error")
        self.assertEqual(self.l4.intersect(self.l3), Point(3, 3),
                         "Computation error")
        self.assertEqual(self.l6.intersect(self.l5), self.l6,
                         "Computation error")
        self.assertEqual(self.l7.intersect(self.l5), False,
                         "Computation error")

    def test_same_point(self):
        self.assertRaises(SamePointError, Line, [Point(0, 0), Point(0, 0)])
        self.assertRaises(SamePointError, Line, [Point(11, 8), Point(11, 8)])

    def tearDown(self):
        super(TestLine, self).tearDown()


if __name__ == '__main__':
    unittest.main()
