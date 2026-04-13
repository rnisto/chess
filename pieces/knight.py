from .piece import Piece
from .utils import BishopMovement, RookMovement, KnightMovement

class Knight(Piece):
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        row, col = pos

        legal_moves = []
        potential_moves = KnightMovement(board,pos)
        for move in potential_moves:
            move_row, move_col = move
            if board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        print(f"Legal moves: {legal_moves}")
        return legal_moves
