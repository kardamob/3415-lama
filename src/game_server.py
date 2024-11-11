import enum

class GamePhase(enum.StrEnum):
    CHOOSE_CARD = "Choose card"
    DRAW_EXTRA = "Draw extra card"
    CHOOSE_CARD_AGAIN = "Choose card again"
    NEXT_PLAYER = "Switch current player"
    END_ROUND = "Round ended"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class GameServer:

    pass