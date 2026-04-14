from .piece import Piece
from .utils import BishopMovement, RookMovement
from math import sqrt

class King(Piece):
    """A Piece that can move one square in any direction, or 'castle'"""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []
        potential_moves = BishopMovement(board,pos) + RookMovement(board,pos)
        for move in potential_moves:
            move_row, move_col = move
            dist = int(sqrt((move_row - row)**2 + (move_col - col)**2))
            if dist > 1: continue
            elif board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        

        print(f"Legal moves: {legal_moves}")
        return legal_moves
