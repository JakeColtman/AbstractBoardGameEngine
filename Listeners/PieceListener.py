from Events.MovementEvent import MovementEvent
from Events.RollbackEvent import RollBackEvent

class PieceListener:

    def __init__(self, piece):
        self.piece = piece
        self.message_history = []
        self.invalid_ids = []

    def recieve_message(self, message):
        if type(message) == RollBackEvent:
            print("Rollback id: {0}".format(message.id))
            self.invalid_ids.append(message.id)
            self.rollback_to_message_id(message.id)
        if type(message) != MovementEvent:
            return
        if message.id in self.invalid_ids:
            return
        self.message_history.append(message)
        self.piece.move_to_pos(message.to_pos)

    def rollback_to_message_id(self, rollback_id):
        complete = False
        if rollback_id not in [x.id for x in self.message_history]:
            return
        while not complete:
            rollingBackMessage = self.message_history.pop()
            if rollingBackMessage.id == rollback_id:
                complete = True
        self.piece.move_to_pos(self.message_history[-1].to_pos)
        print("rolled back to ")
        print(self.piece.pos)
        return True

