from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent
from Game import Game
from Listeners.EndGameListener import EndGameListener
from PieceFactory import PieceFactory
from Events.GameOverEvent import GameOverEvent
from DomainModel.Sides import Sides

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)
bus.register_listener(movement_listener)

piece_factory = PieceFactory(bus)
only_piece = piece_factory.create_piece("Jake", 0)

game = Game()
end_game_listener = EndGameListener(bus, game)
bus.register_listener(end_game_listener)

print(game.state)
bus.broadcast(GameOverEvent(3, Sides.white))
print(game.state)
