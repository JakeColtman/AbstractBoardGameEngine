from DomainModel.Pieces.Piece import Piece
from EventBus import EventBus
from Listeners.PieceListener import PieceListener

class PieceFactory:

    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.max_id = 0

    def create_piece(self, name, pos):
        newId = self.max_id + 1
        piece = Piece(newId, name, pos)
        piece_listener = PieceListener(piece)
        self.event_bus.register_listener(piece_listener)