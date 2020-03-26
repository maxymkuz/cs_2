from flower import *
import unittest


class Test_Flower(unittest.TestCase):
    def setUp(self):
        self.flower1 = Flower('black', 20.0, 10)
        self.flower2 = Flower('blue', 5.7, 20)

    def test_init(self):
        self.assertEqual((self.flower1.color, self.flower2.color),
                         ('black', 'blue'), "Неправильні кольори квіток.")
        self.assertEqual((self.flower1.price, self.flower2.price),
                         (float(20), 5.7), "Ціна має бути дійсним числом.")
        self.assertTrue(self.flower1.price > 0, "Ціна квітки не може бути відємною.")
        self.assertTrue(self.flower2.price > 0, "Ціна квітки не може бути відємною.")
        self.assertTrue(self.flower1.petal > 1, "Квітка має мати хоча б 1 пелюсток.")
        self.assertTrue(self.flower2.petal > 1, "Квітка має мати хоча б 1 пелюсток.")
        self.assertEqual((self.flower1.petal, self.flower2.petal),
                         (int(10.0), int(20.0)), "Кількість пелюсток повинна бути цілою.")


class Test_Tulip(unittest.TestCase):

    def setUp(self):
        self.tulip1 = Tulip('pink', 3.55)
        self.tulip2 = Tulip('purple', 6.7)

    def test_inheritance(self):
        self.assertTrue(isinstance(self.tulip1, Tulip), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.tulip2, Tulip), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.tulip1, Flower), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.tulip2, Flower), "Перевірте приналежність до класу.")

    def test_str(self):
        self.assertEqual(str(self.tulip1), "The pink tulip costs 3.55 and has 15 petals",
                         "Помилка в описі тюльпану.")
        self.assertEqual(str(self.tulip2), "The purple tulip costs 6.7 and has 15 petals",
                         "Помилка в описі тюльпану.")


class Test_Rose(unittest.TestCase):

    def setUp(self):
        self.rose1 = Rose('black', 20.44)
        self.rose2 = Rose('green', 30.7)

    def test_inheritance(self):
        self.assertTrue(isinstance(self.rose1, Rose), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.rose2, Rose), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.rose1, Flower), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.rose2, Flower), "Перевірте приналежність до класу.")

    def test_str(self):
        self.assertEqual(str(self.rose1), "The black rose costs 20.44 and has 41 petals",
                         "Помилка в описі троянди.")
        self.assertEqual(str(self.tulip2), "The green rose costs 30.7 and has 41 petals",
                         "Помилка в описі троянди.")


class Test_Chamomile(unittest.TestCase):

    def setUp(self):
        self.chamomile1 = Chamomile('orange', 2.66)
        self.chamomile2 = Chamomile('white', 1.5)

    def test_inheritance(self):
        self.assertTrue(isinstance(self.chamomile1, Chamomile), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.chamomile2, Chamomile), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.chamomile1, Flower), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.chamomile2, Flower), "Перевірте приналежність до класу.")

    def test_str(self):
        self.assertEqual(str(self.chamomile1), "The orange chamomile costs 2.66 and has 6 petals",
                         "Помилка в описі ромашки.")
        self.assertEqual(str(self.chamomile2), "The white chamomile costs 1.5 and has 6 petals",
                         "Помилка в описі ромашки.")


class Test_FlowerSet(unittest.TestCase):

    def setUp(self):
        self.roses_set = FlowerSet(Rose("red", 15.3), 15)
        self.tulip_set = FlowerSet(Tulip("yellow", 10.05), 5)

    def test_inheritance(self):
        self.assertTrue(isinstance(self.roses_set, Rose), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.tulip_set, Tulip), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.roses_set, Flower), "Перевірте приналежність до класу.")
        self.assertTrue(isinstance(self.roses_set, Flower), "Перевірте приналежність до класу.")

    def test_init(self):
        self.assertTrue(self.roses_set.number > 1, "Набір має містити хоча б одну квітку")
        self.assertTrue(self.tulip_set.number > 1, "Набір має містити хоча б одну квітку")

    def test_price(self):
        self.assertEqual((self.roses_set.price(), self.tulip_set.price()), (15.3 * 15, 10.5 * 5),
                         "Помилка в підрахунку ціни")
        self.assertTrue(type(self.roses_set.price()) == float, "Помилка в підрахунку ціни")
        self.assertTrue(type(self.tulip_set.price()) == float, "Помилка в підрахунку ціни")

    def test_str(self):
        self.assertEqual(str(self.roses_set), "The set of 15 red roses costs 229.5")
        self.assertEqual(str(self.tulip_set), "The set of 5 yellow tulips costs 50.25")


class Test_Bucket(unittest.TestCase):

    def setUp(self):
        self.roses_set = FlowerSet(Rose("red", 15.3), 15)
        self.tulip_set = Floweret(Tulip("yellow", 10.05), 5)
        self.bucket1 = Bucket([self.roses_set, self.tulip_set])

    def test_init(self):
        self.assertTrue(type(self.bucket1.flowers) == list, "Помилка в заданні букету.")
        self.assertTrue(len(self.bucket1.flowers) >= 1, "Букет має мати хоча б один вид квіток.")

    def test_price(self):
        self.assertEqual(self.bucket1.price(), 15.3 * 15 + 10.5 * 5,
                         "Помилка в підрахунку ціни")
        self.assertTrue(type(self.bucket1.price()) == float, "Помилка в підрахунку ціни")

    def test_str(self):
        self.assertEqual(str(self.bucket1), "The bucket of 15 red roses and 5 yellow tulips costs 279.75")


if __name__ == "__main__":
    unittest.main()
