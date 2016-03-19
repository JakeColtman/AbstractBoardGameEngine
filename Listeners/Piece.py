from Events.MovementEvent import MovementEvent

class Piece:

    def __init__(self, id, name, pos):
        self.id, self.name = id, name
        self.pos = pos
        self.message_history = []

    def recieve_message(self, message):
        self.message_history.append(message)
        self._update()

    def _update(self):
        message = self.message_history[-1]
        if type(message) != MovementEvent:
            return
        self.pos = message.to_pos

    def rollback_to_message_id(self, rollback_id):
        complete = False
        if rollback_id not in [x.id for x in self.message_history]:
            raise Exception("Not a valid point in history")
        while not complete:
            rollingBackMessage = self.message_history.pop()
            if rollingBackMessage.id == rollback_id:
                complete = True
            self.pos = rollingBackMessage.from_pos
        return True

