import random
import typing

from src.card import Card


class Deck:
    def __init__(self, cards: None | list[Card]):
        if cards is None:
            # создание новой колоды
            cards = Card.all_cards()
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        if isinstance(other, str):
            other = Deck.load(other)
        return self.cards == other.cards

    def save(self) -> str:
        """Convert deck to string in 'b4 g7 y0' format."""
        list_cards = [c.save() for c in self.cards]  # ['4', '7', '1']
        s = " ".join(list_cards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Convert string in '4 7 0' format to Deck. Return deck."""
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def draw_card(self):
        """Берем карту из колоды и возвращаем ее."""
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def is_empty(self) -> bool:
        """ Проверка пустая ли колода """
        return len(self.cards) == 0
