from DomainModel.Sides import Sides

class GameOverEvent:

    def __init__(self, id, side = Sides.black):
        self.side = side
        self.id = id
