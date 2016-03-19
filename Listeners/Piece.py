from Events.MovementEvent import MovementEvent

class Piece:

    def __init__(self, id, name, pos):
        self.id, self.name = id, name
        self.pos = pos

    def recieve_message(self, message):
        if type(message) != MovementEvent:
            return
        self.pos = message.to_pos
