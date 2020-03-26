class Flower:
    def __init__(self, color, price, petals):
        self.color = color
        self.price = float(price)
        self.petals = int(petals)


class Tulip(Flower):
    def __init__(self, color, price, petals):
        super().__init__(color, price, petals)


class Rose(Flower):
    def __init__(self, color, price, petals):
        super().__init__(color, price, petals)


class Chamomile(Flower):
    def __init__(self, color, price, petals):
        super().__init__(color, price, petals)

class FlowerSet:
    def __init__(self, flower, count):
        self.flower = flower
        self.count = count

    def price(self):
        return self.flower.price * self.count


class Bucket:
    def __init__(self, flowerSets):
        self.flowerSets = flowerSets

    def price(self):
        return float(sum([i.flower.price * i.count for i in self.flowerSets]))