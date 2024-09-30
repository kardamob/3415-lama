"""Карты LAMA."""
from typing import Self


class Card:
    NUMBERS = list(range(1,8))
    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        self.number = number

    def __repr__(self):
        # '6'
        return f'{self.number}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.number == other.number

    # def __lt__(self, other):
    #     if self.number == other.number or self.number == other.number + 1:
    #         return self.number < other.number
    #     ind_self = self.NUMBERS.index(self.number)
    #     ind_other = self.NUMBERS.index(other.number)
    #     return ind_self < ind_other

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From '3' to Card(3)."""
        return Card(number=int(text[0]))

    def can_play_on(self, other: Self) -> bool:
        """Можно ли играть карту self на карту other."""
        return  self.number == other.number or self.number == other.number + 1

    @staticmethod
    def all_cards(numbers: None | list[int] = None):
        if numbers is None:
            numbers = Card.NUMBERS
        # cards = []
        # for i in range(8):
        #     for num in numbers:
        #         cards.append(Card(number=num))
        cards = [Card(number=num) for i in range(8) for num in numbers]
        return cards

    def score(self):
        """Штрафные очки за карту."""
        if self.number < 7:
            return self.number
        # else:
        #     return 10
        return 10
