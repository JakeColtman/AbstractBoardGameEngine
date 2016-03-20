from Events.MovementEvent import MovementEvent
from Events.RollbackEvent import RollBackEvent

class Piece:

    def __init__(self, id, name, pos):
        self.id, self.name = id, name
        self.pos = pos

    def move_to_pos(self, pos: int):
        self.pos = pos

