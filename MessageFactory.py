from Events.GameOverEvent import GameOverEvent
from Events.EndOfTurnEvent import EndOfTurnEvent
from Events.MovementEvent import MovementEvent
from Events.RollbackEvent import RollBackEvent

class MessageFactory:

    def __init__(self):
        self.max_id = -1

    def create_gameover_event(self, side, prev = None):
        if prev is None:
            self.max_id += 1
            id = self.max_id
        else:
            id = prev.id

        return GameOverEvent(id, side)

    def create_movement_event(self, from_pos, to_pos, prev = None):
        if prev is None:
            self.max_id += 1
            id = self.max_id
        else:
            id = prev.id

        return MovementEvent(id, from_pos, to_pos)

    def create_end_of_turn_event(self, prev = None):
        if prev is None:
            self.max_id += 1
            id = self.max_id
        else:
            id = prev.id

        return EndOfTurnEvent(id)

    def create_rollback_event(self, prev = None):
        if prev is None:
            self.max_id += 1
            id = self.max_id
        else:
            id = prev.id

        return RollBackEvent(id)