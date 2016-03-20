from EventBus import EventBus
from Game import Game
from Events.EndOfTurnEvent import EndOfTurnEvent
from DomainModel.Sides import Sides

class EndOfTurnListener:

    def __init__(self, event_bus, game: Game):
        self.event_bus = event_bus
        self.game = game

    def recieve_message(self, message):
        if type(message) != EndOfTurnEvent:
            return
        if self.game.turn == Sides.white:
            self.game.turn = Sides.black
        else:
            self.game.turn = Sides.white
