from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent
from Listeners.PieceListener import PieceListener
from DomainModel.Pieces.Piece import Piece

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)
only_piece = Piece(1, "Jake", 3)
only_piece_listener = PieceListener(only_piece)
bus.register_listener(movement_listener)
bus.register_listener(only_piece_listener)

print(only_piece.pos)
bus.broadcast(MovementEvent(1, 3, 4))
bus.broadcast(MovementEvent(2, 4, 5))
print(only_piece.pos)
