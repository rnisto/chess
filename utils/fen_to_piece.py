from pieces import Pawn, Rook, Bishop, Queen, King, Knight

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
    colour, type, image = piece_map[char]

    if type == "p":
        return Pawn(colour, type, image)
    elif type == "r":
        return Rook(colour, type, image)
    elif type == "b":
        return Bishop(colour, type, image)
    elif type == "q":
        return Queen(colour, type, image)
    elif type == "k":
        return King(colour, type, image)
    elif type == "n":
        return Knight(colour, type, image)
    return None
