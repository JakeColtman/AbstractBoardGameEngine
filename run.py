from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent

from PieceFactory import PieceFactory

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)
bus.register_listener(movement_listener)

piece_factory = PieceFactory(bus)
only_piece = piece_factory.create_piece("Jake", 0)

print(only_piece.pos)
bus.broadcast(MovementEvent(1, 3, 4))
bus.broadcast(MovementEvent(2, 4, 10))
print(only_piece.pos)
