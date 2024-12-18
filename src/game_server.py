import enum
import inspect
import json
import sys
from pathlib import Path

from src.deck import Deck
from src.game_state import GameState
from src.hand import Hand
from src.player import Player

class GamePhase(enum.StrEnum):
    GAME_START = "Game starts"
    CHOOSE_CARD = "Choose card"
    DRAW_EXTRA = "Draw extra card"
    CHOOSE_CARD_AGAIN = "Choose card again"
    NEXT_PLAYER = "Switch current player"
    PLAYER_QUIT = "Player ends his turn"
    BEGIN_ROUND = "Round begins"
    END_ROUND = "Round ended"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class GameServer:

    pass