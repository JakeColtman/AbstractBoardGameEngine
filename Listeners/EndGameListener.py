from EventBus import EventBus
from Game import Game
from Events.GameOverEvent import GameOverEvent

class EndGameListener:

    def __init__(self, event_bus, game: Game):
        self.event_bus = event_bus
        self.game = game

    def recieve_message(self, message):
        if type(message) != GameOverEvent:
            return
        self.game.finish_game(message.side)
