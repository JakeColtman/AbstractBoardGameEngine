
class MovementEvent:

    def __init__(self, id, piece_id, to_pos):
        self.id = id
        self.piece_id, self.to_pos = piece_id, to_pos