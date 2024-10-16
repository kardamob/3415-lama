import typing

from src.card import Card


class Hand:
    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            # может быть пустая рука
            cards = []
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        if isinstance(other, str):
            other = Hand.load(other)
        return self.cards == other.cards

    def save(self) -> str:
        """Convert deck to string in '4 7 1' format."""
        scards = [c.save() for c in self.cards]  # ['4', '7', '1']
        s = " ".join(scards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Convert string in '4 7 1' format to Deck. Return deck."""
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def score(self):
        """Штрафные очки"""
        score = 0 # счет очков
        unique_cards = set(self.cards)
        for c in unique_cards:
            score += c.score()
        return score

    def playable_cards(self, top_card: Card) -> [Card]:
        """Какие карты можно сыграть"""
        return [c for c in self.cards if c.can_play_on(top_card)]