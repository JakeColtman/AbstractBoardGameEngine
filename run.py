from EventBus import EventBus
from Listeners.Movement import Board

movement_listener = Board()
bus = EventBus()
bus.register_listener(movement_listener)

bus.broadcast("Hello world")