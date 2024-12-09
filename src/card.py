"""Карты LAMA."""

from typing import Self


class Card:
    NUMBERS = list(range(1, 8))
    # usual cards = 1,2,3,4,5,6 | unusual card (Lama) = 7
    max_value_of_usual_cards = 6
    score_of_lama = 10
    count_cards_of_one_type = 8
    count_of_types = 7

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        self.number = number

    def __repr__(self):
        return f"{self.number}"

    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.number == other.number

    def __lt__(self, other):
        if self.number == other.number or self.number == other.number + 1:
            return self.number < other.number
        ind_self = self.NUMBERS.index(self.number)
        ind_other = self.NUMBERS.index(other.number)
        return ind_self < ind_other

    def __hash__(self):
        return self.number

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From '4' to Card(4)."""
        return Card(number=int(text[0]))

    def can_play_on(self, other: Self) -> bool:
        """Можно ли играть карту self на карту other."""
        if self.number <= Card.max_value_of_usual_cards:
            return  self.number == other.number or self.number == other.number + 1
        return self.number == other.number or self.number == 1

    @staticmethod
    def all_cards(numbers: None | list[int] = None):
        if numbers is None:
            numbers = Card.NUMBERS
        # cards = []
        # for i in range(Card.count_cards_of_one_type):
        #     for num in numbers:
        #         cards.append(Card(number=num))
        cards = [
            Card(number=num)
            for _ in range(Card.count_cards_of_one_type)
            for num in numbers
        ]
        return cards

    def score(self):
        """Штрафные очки за карту."""
        if self.number <= Card.max_value_of_usual_cards:
            return self.number
        # else:
        #     return Card.score_of_lama (= 10)
        return Card.score_of_lama
