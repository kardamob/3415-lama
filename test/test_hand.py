from src.card import Card
from src.hand import Hand

cards = [Card(3), Card(1), Card(7)]


def test_init():
    d = Hand(cards=cards)
    assert d.cards == cards


def test_save():
    d = Hand(cards=cards)
    assert d.save() == "3 1 7"

    d = Hand(cards=[])
    assert d.save() == ""


def test_load():
    d = Hand.load("3 1 7")
    expected_deck = Hand(cards)
    assert d == expected_deck


def test_score():
    h = Hand.load("3 3 1 7 7") # 7 - Лама (10 очков)
    assert h.score() == 14

    h = Hand.load("2 4")
    assert h.score() == 6


def test_add_card():
    h = Hand.load("3 1 7")
    h.add_card(Card.load("2"))
    assert repr(h) == "3 1 7 2"

    h.add_card(Card.load("5"))
    assert repr(h) == "3 1 7 2 5"


def test_remove_card():
    h = Hand.load("3 1 7 2 5")
    c = Card.load("7")
    h.remove_card(c)
    assert repr(h) == "3 1 2 5"

def test_markers():
    h = Hand.load("3 3 1 7 7")
    assert Hand.markers(h) == (1, 4)

    h = Hand.load("7 7 7 7 7")
    assert Hand.markers(h) == (1, 0)

    h = Hand.load("2 7 6 5 5")
    assert Hand.markers(h) == (2, 3)