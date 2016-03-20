from Events.MovementEvent import MovementEvent
from Events.RollbackEvent import RollBackEvent
from MessageFactory import MessageFactory

class MovemetOutBounds:

    def __init__(self, event_bus, message_factory:MessageFactory, size = 5):
        self.lower_limit, self.upper_limit = 0, 5
        self.event_bus = event_bus
        self.message_factory = message_factory

    def recieve_message(self, message):
        if type(message) != MovementEvent:
            return
        if message.to_pos > self.upper_limit:
            self.event_bus.broadcast(self.message_factory.create_rollback_event(message))