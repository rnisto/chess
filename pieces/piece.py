class Piece:
    """An object with defined movement rules around the board"""
    def __init__(self, colour, type, image):
        self.colour = colour
        self.type = type
        self.image = image

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        return []