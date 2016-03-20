from DomainModel.Sides import Sides
from DomainModel.GameState import GameState


class Game:
    def __init__(self):
        self.turn = Sides(0)
        self.state = GameState(0)
        self.winning_side = None

    def start_game(self):
        self.state = GameState.in_progress

    def finish_game(self, winning_side: Sides):
        self.winning_side = winning_side
        self.state = GameState.finished
