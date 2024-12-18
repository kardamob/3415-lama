import typing
import math

from src.card import Card


class Hand:
    def __init__(self, cards: list[Card] = None):
        if cards is None:
            # может быть пустая рука
            cards = []
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        """ """
        if isinstance(other, str): # если переменная other - str, то
            other = Hand.load(other) # переприсваиваем переменной other значение метода load класса Hand
        return self.cards == other.cards # возвращаем

    def save(self) -> str:
        """Конвертирует колоду в '4 7 1' формат."""
        list_cards = [c.save() for c in self.cards]  # ['4', '7', '1']
        s = " ".join(list_cards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Конвертирует строку '4 7 1' формата в класс Deck. Возвращает обратно атрибут класса Deck."""
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card: Card):
        """Добавляет карту в руку"""
        self.cards.append(card)

    def remove_card(self, card: Card):
        """Удаляет карту из руки"""
        self.cards.remove(card)

    def score(self):
        """Штрафные очки"""
        score = 0
        unique_cards = set(self.cards)
        for c in unique_cards:
            score += c.score()
        return score

    def playable_cards(self, top_card: Card) -> [Card]:
        """Какие карты можно сыграть"""
        return [c for c in self.cards if c.can_play_on(top_card)]

    @staticmethod
    def markers(score):
        """Подсчет маркеров"""
        if score < 10:
            white_markers = score
            black_markers = 0
            return black_markers, white_markers
        else:
            black_markers = math.floor(score/10)
            white_markers = score - black_markers*10
            return black_markers, white_markers

    @staticmethod
    def clear():
        return list()
