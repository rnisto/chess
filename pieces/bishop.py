from .piece import Piece
from .utils import BishopMovement

class Bishop(Piece):
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        row, col = pos

        # use self, not board lookup
        direction = 1 if self.colour == "b" else -1

        legal_moves = []

        for move in BishopMovement(board,pos):
            move_row, move_col = move
            if board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        print(f"Legal moves: {legal_moves}")
        return legal_moves
