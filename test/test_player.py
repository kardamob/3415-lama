from src.hand import Hand
from src.player import Player


def test_init():
    h = Hand.load("1 3 2")
    p = Player(name="Alex", hand=h, score=10)
    assert p.name == "Alex"
    assert p.hand == h
    assert p.score == 10


def test_str():
    h = Hand.load("1 3 2")
    p = Player(name="Alex", hand=h, score=15)
    assert str(p) == "Alex(15): 1 3 2"


def test_save():
    h = Hand.load("1 3 2")
    p = Player(name="Alex", hand=h, score=15)
    assert p.save() == {"name": "Alex", "score": 15, "hand": "1 3 2"}


def test_eq():
    h1 = Hand.load("1 3 2")
    h2 = Hand.load("1 3 2")
    p1 = Player(name="Alex", hand=h1, score=10)
    p2 = Player(name="Alex", hand=h2, score=10)
    assert p1 == p2
    h1 = Hand.load("1 3 2")
    h2 = Hand.load("1 3 2")
    p1 = Player(name="Ivan", hand=h1, score=10)
    p2 = Player(name="Alex", hand=h2, score=10)
    assert p1 != p2


def test_load():
    data = {"name": "Alex", "score": 10, "hand": "1 3 2"}
    h = Hand.load("1 3 2")
    p_expected = Player(name="Alex", hand=h, score=10)
    p = Player.load(data)
    assert p == p_expected