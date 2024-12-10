from src.card import Card
from src.deck import Deck
from src.game_state import GameState
from src.hand import Hand
from src.player import Player

data = {
    "top": "7",
    "current_player_index": 1,
    "deck": "5",
    "players": [
        {"name": "Alex", "hand": "3 6", "score": 5},
        {"name": "Bob", "hand": "5", "score": 1},
        {"name": "Charley", "hand": "7 1 2", "score": 3},
    ],
}

alex = Player.load(data["players"][0])
bob = Player.load(data["players"][1])
charley = Player.load(data["players"][2])
full_deck = Deck(None)


def test_init(): #Проверяет инициализацию состояния игры
    players = [alex, bob, charley]
    test_game = GameState(players=players, deck=full_deck, current_player=2, top=Card.load("2"))

    assert test_game.players == players
    assert test_game.deck == full_deck
    assert test_game.current_player() == charley
    assert str(test_game.top) == "2"


def test_current_player():
    players = [alex, bob, charley]

    game = GameState(players=players, deck=full_deck, top=Card.load("3")) #current_player=0 можно не указывать, тк по умолчанию стоит 0
    assert game.current_player() == alex

    game = GameState(players=players, deck=full_deck, top=Card.load("3"), current_player=1)
    assert game.current_player() == bob

    game = GameState(players=players, deck=full_deck, top=Card.load("3"), current_player=2)
    assert game.current_player() == charley


def test_eq():
    players = [alex, bob, charley]
    game1 = GameState(players=players, deck=full_deck, top=Card.load("4"))
    game1_copy = GameState(players=players.copy(), deck=Deck(game1.deck.cards.copy()), top=Card.load("4"))
    game2 = GameState(players=players.copy(), deck=Deck(None), top=Card.load("4"))
    game3 = GameState(players=players, deck=Deck.load("2 6 1"), top=Card.load("4"))
    assert game1 == game1_copy
    assert game1 != game2       # shuffled Deck
    assert game1 != game3


def test_save():
    players = [alex, bob, charley]
    game = GameState(
        players=players,
        deck=Deck.load(data["deck"]),
        top=Card.load(data["top"]),
        current_player=1,
    )
    assert game.save() == data


def test_load():
    data_game = GameState.load(data)
    players_info = [Player(name="Alex",hand=Hand([Card(3), Card(6)]), score=5),
                    Player(name="Bob",hand=Hand([Card(5)]), score=1),
                    Player(name="Charley",hand=Hand([Card(7), Card(1), Card(2)]), score=3)]
    assert data_game == GameState(players=players_info, deck=Deck([Card(5)]), top=Card(7), current_player=1)
    assert data_game.save() == data


def test_next_player():
    game = GameState.load(data)
    assert game.current_player() == bob

    game.next_player()
    assert game.current_player() == charley

    game.next_player()
    assert game.current_player() == alex

    game.next_player()
    assert game.current_player() == bob

def test_draw_card():
    game = GameState.load(data)
    assert game.deck == "5"
    assert game.current_player().hand == "g5"

    game.draw_card()
    assert game.deck == "g2 y6"
    assert game.current_player().hand == "g5 b0"