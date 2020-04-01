class TextMachine:
    """ Representrs a texting machine"""
    def __init__(self, tup1, tup2):
        self.texts1 = tup1[0]
        self.texts_price = tup1[1]
        self.texts2 = tup2[0]
        self.texts2_price = tup2[1]
        self.owed1 = self.texts_price
        self.owed2 = self.texts2_price

    def __str__(self):
        price1 = self.add_zero(self.texts_price/100)
        price2 = self.add_zero(self.texts2_price/100)
        if self.texts2 == 0:
            return f"Text Machine:<{self.texts1} texts; ₴{price1} each>"
        return f"Text Machine:<{self.texts1} texts; ₴{price1} " \
               f"each>;" \
               f" <{self.texts2} texts; ₴{price2} each>"

    def get_text_count(self):
        return self.texts1, self.texts2

    @staticmethod
    def add_zero(price):
        """ Adds zero if nessesary"""
        price = str(price)
        if len(price.split('.')[1]) == 1:
            price += '0'
        return price

    def is_empty(self):
        """ Ret true if empty"""
        if self.get_text_count()[0] == 0 and self.get_text_count()[1] == 0:
            return True
        return False

    def still_owe(self):
        return self.owed1, self.owed2

    def insert_money(self, tup):
        """
        Makes all the tranzactions needed for a machine
        """
        if tup[1] == "short":
            if self.texts1 == 0:
                return "Machine is empty", tup[0]

            self.owed1 = self.owed1 - tup[0]
            if self.owed1 > 0:
                return f"Still owe ₴{self.add_zero(self.owed1/100)}", \
                       self.texts_price \
                       - \
                       self.owed1
            elif self.owed1 <= 0:
                self.texts1 -= 1
                self.owed1 = self.texts_price
                self.owed2 = self.texts2_price
                return ("Got a text!", self.texts_price)
            elif self.owed1 < 0:
                reshta = - self.owed1
                self.texts1 -= 1
                self.owed1 = self.texts_price
                return ("Got a text!", reshta)
        if tup[1] == "long":
            if self.texts2 == 0:
                return "Machine is empty", tup[0]
            self.owed2 = self.owed2 - tup[0]
            if self.owed2 > 0:
                return f"Still owe ₴{round(self.owed2/100, 2)}", \
                       self.texts2_price - self.owed2
            elif self.owed2 == 0:
                self.texts2 -= 1
                self.owed2 = self.texts2_price
                return ("Got a text!", self.texts_price)
            elif self.owed2 < 0:
                reshta = - self.owed2
                self.texts2 -= 1
                self.owed2 = self.texts2_price
                return ("Got a text!", reshta)

    @classmethod
    def airport_machine(cls):
        return TextMachine((200, 225), (200, 345))

    def stock_machine(self, tup):
        self.texts1 += tup[0]
        self.texts2 += tup[1]

    def __eq__(self, other):
        if not isinstance(other, TextMachine):
            return True
        if self.texts1 == other.texts1 and self.texts2 == other.texts2:
            if self.texts_price == other.texts_price and self.texts2_price \
                    == other.texts2_price:
                return True
        return False

    def __ne__(self, other):
        if not isinstance(other, TextMachine):
            return True
        if self.texts1 == other.texts1 and self.texts2 == other.texts2:
            if self.texts_price == other.texts_price and self.texts2_price \
                    == other.texts2_price:
                return False
        return True

    def __contains__(self, item):
        for i in item:
            if self.texts1 == i.texts1 and self.texts2 == i.texts2:
                if self.texts_price == i.texts_price and self.texts2_price \
                        == i.texts2_price:
                    return True
        return False

    def __hash__(self):
        return 1