from Events.MovementEvent import MovementEvent
from Events.RollbackEvent import RollBackEvent

class MovemetOutBounds:

    def __init__(self, event_bus, size = 5):
        self.lower_limit, self.upper_limit = 0, 5
        self.event_bus = event_bus

    def recieve_message(self, message):
        if type(message) != MovementEvent:
            return
        if message.to_pos > self.upper_limit:
            self.event_bus.broadcast(RollBackEvent(message.id))