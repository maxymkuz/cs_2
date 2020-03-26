import unittest
from all_prefixes import all_prefixes, NotASingleWordError, NotAStringError


class TestAllPrefixes(unittest.TestCase):
    def test_wrong_type_input(self):
        ipt_1 = ["авангард"]
        ipt_2 = 1234
        ipt_3 = 1234.56789
        ipt_4 = {1: 'a', 2: 'b'}
        self.assertRaises(NotAStringError, all_prefixes, ipt_1)
        self.assertRaises(NotAStringError, all_prefixes, ipt_2)
        self.assertRaises(NotAStringError, all_prefixes, ipt_3)
        self.assertRaises(NotAStringError, all_prefixes, ipt_4)

    def test_wrong_input(self):
        """
        Test a function with all possible WRONG STRING inputs
        """
        self.assertRaises(NotASingleWordError, all_prefixes, "")
        self.assertRaises(NotASingleWordError, all_prefixes, "These are "
                                                             "two words")

        self.assertRaises(NotASingleWordError, all_prefixes, "A sentence")

    def test_usual_case(self):
        self.assertEqual(all_prefixes("lead"), {'le', 'l', 'lea', 'lead'})
        self.assertEqual(all_prefixes("max"), {'m', 'ma', 'max'})

    def test_with_multiple_first_letters(self):
        self.assertEqual(all_prefixes("авангард"),
                         {'а', 'ар', 'аван', 'аванг', 'ава', 'ан',
                          'ангар', 'ангард', 'авангар', 'анга',
                          'ард', 'анг', 'ав', 'авангард', 'аванга'})
        self.assertEqual(all_prefixes("Kuzyshyn"),
                         {'kuzy', 'ku', 'kuz', 'kuzyshyn', 'kuzyshy', 'kuzys',
                          'kuzysh', 'k'})

    def test_uppercase(self):
        self.assertEqual(all_prefixes("LeAD"), {'le', 'l', 'lea', 'lead'})
        self.assertEqual(all_prefixes("KuzYshYN"),
                         {'kuzy', 'ku', 'kuz', 'kuzyshyn', 'kuzyshy', 'kuzys',
                          'kuzysh', 'k'})
        self.assertEqual(all_prefixes("АвангАрД"),
                         {'а', 'ар', 'аван', 'аванг', 'ава', 'ан',
                          'ангар', 'ангард', 'авангар', 'анга',
                          'ард', 'анг', 'ав', 'авангард', 'аванга'})


if __name__ == '__main__':
    unittest.main()
