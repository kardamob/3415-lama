import pytest

from src.card import Card

def test_init():
    c = Card(3)
    assert c.number == 3


def test_save():
    c = Card(3)
    assert repr(c) == '3'
    assert c.save() == '3'

    c = Card(7)
    assert repr(c) == '7'
    assert c.save() == '7'


def test_eq():
    c1 = Card(2)
    c2 = Card(2)
    c3 = Card(1)
    c4 = Card(3)
    c5 = Card(7)

    assert c1 == c2
    assert c1 != c3
    assert c1 != c4
    assert c2 != c5


def test_load():
    s = '5'
    c = Card.load(s)
    assert c == Card(5)

    s = '7'
    c = Card.load(s)
    assert c == Card(7)


def test_divzero():
    # пример теста с ловлей исключения
    with pytest.raises(ZeroDivisionError):
        x = 2 / 0
        # y = 3 / 15


def test_validation():
    with pytest.raises(ValueError):
        Card(1)
    with pytest.raises(ValueError):
        Card(10)
    with pytest.raises(ValueError):
        Card('3')


def test_play_on():
    c1 = Card.load('1')
    c2 = Card.load('2')
    c3 = Card.load('3')
    c4 = Card.load('4')

    assert c1.can_play_on(c1)
    assert c2.can_play_on(c1)
    assert c2.can_play_on(c2)
    assert c3.can_play_on(c2)
    assert not c4.can_play_on(c1)


def test_all_cards():
    cards = Card.all_cards(numbers=[5, 2, 7])
    # print(cards)
    expected_cards = [
        Card.load('5'),
        Card.load('2'),
        Card.load('7'),
    ]
    assert cards == expected_cards

    cards = Card.all_cards()
    assert len(cards) == 8 * 7


def test_score():
    c = Card(7)
    assert 7 == c.score()
    c = Card(3)
    assert 3 == c.score()