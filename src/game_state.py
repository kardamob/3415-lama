import typing

from src.card import Card
from src.deck import Deck
from src.player import Player

class GameState:
    def __init__(
            self, players: list[Player], deck: Deck, top: Card, current_player: int = 0
    ):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self.top: Card = top
        self.__current_player: int = current_player

    @property #свойство класса
    def current_player_index(self):   # возвращает индекс текущего игрока
        return self.__current_player

    def current_player(self) -> Player: # возвращает
        return self.players[self.__current_player]

    def __eq__(self, other):
        # return self.players == other.players and self.deck == other.deck and self.top == other.top and \
        #         self._current_player == other._current_player
        if self.players != other.players:
            return False
        if self.deck != other.deck:
            return False
        if self.top != other.top:
            return False
        if self.__current_player != other.__current_player:
            return False
        return True

    def save(self) -> dict: # возвращает состояние игрока
        return {
            "top": str(self.top),
            "deck": str(self.deck),
            "current_player_index": self.__current_player,
            "players": [p.save() for p in self.players],
        }

    @classmethod
    def load(cls, data: dict):
        """
        data = {
            'top': '7',
            'current_player_index': 1,
            'deck': '2 6 0',
            'players': [
                {
                    'name': 'Alex',
                    'hand': '3 6',
                    'score': 5
                },
                {
                    'name': 'Bob',
                    'hand': '5',
                    'score': 1
                },
                {
                    'name': 'Charley',
                    'hand': '7 1 2',
                    'score': 3
                }
            ]
        }
        """
        players = [Player.load(d) for d in data["players"]]

        return cls(
            players=players,
            deck=Deck.load(data["deck"]),
            top=Card.load(data["top"]),
            current_player=int(data["current_player_index"]),
        )

    def next_player(self):
        """Ход переходит к следующему игроку."""
        n = len(self.players)
        self.__current_player = (self.__current_player + 1) % n

    def draw_card(self) -> Card:
        """Текущий игрок берет карту из колоды."""
        card = self.deck.draw_card()
        self.current_player().hand.add_card(card)
        return card

    def play_card(self, card: Card):
        """Карта card от текущего игрока переходит в top."""
        self.current_player().hand.remove_card(card)
        self.top = card

    def player_action(self):
        """Обработка действий текущего игрока."""
        current_player = self.current_player()
        print(f"{current_player.name}: {current_player.hand}")
        while True:
            action = input(f"{current_player.name}, выберите действие (играть/взять/сбросить): ").strip().lower()
            if action == "играть":
                card_value = input("Введите значение карты, которую хотите сыграть: ")
                try:
                    card = Card(int(card_value))  # Пробуем создать карту
                    if card in current_player.hand.cards:
                        self.play_card(card)
                        print(f"{current_player.name} играет {card}")
                        break
                    else:
                        print("Такой карты нет в руке.")
                except ValueError:
                    print("Недопустимое значение карты.")
            elif action == "взять":
                self.draw_card()
                print(f"{current_player.name} берет карту.")
                break
            elif action == "сбросить":
                current_player.hand.clear()  # Убираем карты игрока
                print(f"{current_player.name} сбрасывает карты.")
                break
            else:
                print("Данного действия не существует. Попробуйте ввести одну из следующих команд: играть/взять/сбросить")
