from .piece import Piece
from .utils import RookMovement

class Rook(Piece):
    """A Piece that can move to any square horizontally or diagonally."""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []

        for move in RookMovement(board,pos):
            move_row, move_col = move
            if board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        print(f"Legal moves: {legal_moves}")
        return legal_moves
