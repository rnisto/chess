"""A set of functions to parse fen strings"""

import pieces.classes

# A map of fen characters to Pieces.
piece_map = {
    'p': ('b', 'p', './pieces/assets/bp.png'),
    'P': ('w', 'p', './pieces/assets/wp.png'),
    'r': ('b', 'r', './pieces/assets/br.png'),
    'R': ('w', 'r', './pieces/assets/wr.png'),
    'n': ('b', 'n', './pieces/assets/bn.png'),
    'N': ('w', 'n', './pieces/assets/wn.png'),
    'b': ('b', 'b', './pieces/assets/bb.png'),
    'B': ('w', 'b', './pieces/assets/wb.png'),
    'q': ('b', 'q', './pieces/assets/bq.png'),
    'Q': ('w', 'q', './pieces/assets/wq.png'),
    'k': ('b', 'k', './pieces/assets/bk.png'),
    'K': ('w', 'k', './pieces/assets/wk.png'),
}

# piece_map = {
#     'p': ('b', 'p', 'p'),
#     'P': ('w', 'p', 'P'),
#     'r': ('b', 'r', 'r'),
#     'R': ('w', 'r', 'R'),
#     'n': ('b', 'n', 'n'),
#     'N': ('w', 'n', 'N'),
#     'b': ('b', 'b', 'b'),
#     'B': ('w', 'b', 'B'),
#     'q': ('b', 'q', 'q'),
#     'Q': ('w', 'q', 'Q'),
#     'k': ('b', 'k', 'k'),
#     'K': ('w', 'k', 'K'),
# }

def FenToPiece(char):
    """This function takes a fen character and returns the relevant
    class."""
    colour, type, image = piece_map[char]

    if type == "p":
        return pieces.classes.Pawn(colour, type, image)
    elif type == "r":
        return pieces.classes.Rook(colour, type, image)
    elif type == "b":
        return pieces.classes.Bishop(colour, type, image)
    elif type == "q":
        return pieces.classes.Queen(colour, type, image)
    elif type == "k":
        return pieces.classes.King(colour, type, image)
    elif type == "n":
        return pieces.classes.Knight(colour, type, image)
    return None
