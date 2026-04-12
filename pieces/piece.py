class Piece:
    def __init__(self, colour, type, image):
        self.colour = colour
        self.type = type
        self.image = image

    def get_legal_moves(self, board, pos):
        return []