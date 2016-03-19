
class Board:

    def __init__(self, size = 5):
        self.lower_bound, self.upper_bound = 0, 5

    def recieve_message(self, message):
        print(message)