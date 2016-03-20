from enum import Enum


class Turn(Enum):
    white = 0
    black = 1


class Game:
    def __init__(self):
        self.turn = "White"