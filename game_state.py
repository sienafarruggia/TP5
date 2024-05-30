from enum import Enum

import arcade


class GameState(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROUND_DONE = 0,
   GAME_OVER = 1,
   NOT_STARTED = 2,
   ROUND_ACTIVE = 3,