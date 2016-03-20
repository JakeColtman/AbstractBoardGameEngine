from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent
from Game import Game
from Listeners.EndGameListener import EndGameListener
from PieceFactory import PieceFactory
from Events.GameOverEvent import GameOverEvent
from DomainModel.Sides import Sides
from DomainModel.GameState import GameState
from MessageFactory import MessageFactory

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)
bus.register_listener(movement_listener)

piece_factory = PieceFactory(bus)
only_piece = piece_factory.create_piece("Jake", 0)

game = Game()
end_game_listener = EndGameListener(bus, game)
bus.register_listener(end_game_listener)

message_factory = MessageFactory()

print("Input your move1")
while game.state != GameState.finished:
    new_pos = int(input())
    bus.broadcast(message_factory.create_movement_event(0, new_pos))
    if only_piece.pos == 3:
        bus.broadcast(GameOverEvent(1, Sides.white))
print("Game over - you win")
