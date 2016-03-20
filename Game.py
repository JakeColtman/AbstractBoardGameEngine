from enum import Enum


class Sides(Enum):
    white = 0
    black = 1


class GameState(Enum):
    not_started = 0
    in_progress = 1
    finished = 2


class Game:
    def __init__(self):
        self.turn = "White"
