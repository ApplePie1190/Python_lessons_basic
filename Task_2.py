from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_fabric_result = 0

    @abstractmethod
    def fabric_result(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.sum_fabric_result += self.fabric_result

    def __str__(self):
        return f'Для пальто размера {self.size} расход ткани составил: {self.fabric_result}, ' \
               f'суммарный расход: {round(Coat.sum_fabric_result, 2)}'

    @property
    def fabric_result(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.sum_fabric_result += self.fabric_result

    def __str__(self):
        return f'Для костюма на рост {self.height} расход ткани составил: {self.fabric_result}, '\
               f'суммарный расход ткани: {round(Suit.sum_fabric_result, 2)}'

    @property
    def fabric_result(self):
        return round(self.height * 2 + 0.3, 2)


coat_1 = Coat(3)
suit_1 = Suit(2)
suit_2 = Suit(3)
print(coat_1)
print(suit_1)
print(suit_2)
