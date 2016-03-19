from EventBus import EventBus
from Listeners.Movement import MovementListener

movement_listener = MovementListener()
bus = EventBus()
bus.register_listener(movement_listener)

bus.broadcast("Hello world")