from EventBus import EventBus
from Listeners.Movement.MovementOutOfBounds import MovemetOutBounds
from Events.MovementEvent import MovementEvent

bus = EventBus()
movement_listener = MovemetOutBounds(bus, 5)

bus.register_listener(movement_listener)

bus.broadcast(MovementEvent(1, 0, 10))