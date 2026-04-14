import pieces

piece_map = {
    'p': ('b', 'p', 'p'),
    'P': ('w', 'p', 'P'),
    'r': ('b', 'r', 'r'),
    'R': ('w', 'r', 'R'),
    'n': ('b', 'n', 'n'),
    'N': ('w', 'n', 'N'),
    'b': ('b', 'b', 'b'),
    'B': ('w', 'b', 'B'),
    'q': ('b', 'q', 'q'),
    'Q': ('w', 'q', 'Q'),
    'k': ('b', 'k', 'k'),
    'K': ('w', 'k', 'K'),
}

def FenToPiece(char):
    """This function takes a fen character and returns the relevant
    class."""
    colour, type, image = piece_map[char]

    if type == "p":
        return pieces.Pawn(colour, type, image)
    elif type == "r":
        return pieces.Rook(colour, type, image)
    elif type == "b":
        return pieces.Bishop(colour, type, image)
    elif type == "q":
        return pieces.Queen(colour, type, image)
    elif type == "k":
        return pieces.King(colour, type, image)
    elif type == "n":
        return piences.Knight(colour, type, image)
    return None
