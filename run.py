from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent
from Listeners.Piece import Piece

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)
only_piece = Piece(1, "Jake", 3)
bus.register_listener(movement_listener)
bus.register_listener(only_piece)

print(only_piece.pos)
bus.broadcast(MovementEvent(1, 3, 4))
bus.broadcast(MovementEvent(2, 4, 10))
print(only_piece.pos)
