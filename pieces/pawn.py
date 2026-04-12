from .piece import Piece
from .utils import PerpendicularMovement

class Pawn(Piece):
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        row, col = pos

        # use self, not board lookup
        direction = 1 if self.colour == "b" else -1
        
        # pawns can move up to 2 squares
        if (self.colour == "w" and col == 6) or (self.colour == "b" and col == 1):
            distance = 2 
        else: distance = 1

        legal_moves = []

        perpendicular_moves = PerpendicularMovement(board,pos)
        for move in perpendicular_moves:
            move_row, move_col = move
            if (abs(move_col - col) <= distance) and (move_col - col)*direction > 0 and board[move_col][move_row] is None:
                legal_moves.append(move)
            else:
                continue

        # pawns can capture diagonally   
        for i in [-1,1]:
            new_col = col + direction
            new_row = row + i
            
            if new_col > 7 or new_col < 0: continue
            if new_row > 7 or new_row < 0: continue
            print(new_row)
            if board[new_col][new_row] is not None:
                print(f"capture available at ({new_row},{new_col})")
                if (board[new_col][new_row].colour is not self.colour) and (0 <= new_col < 8 and 0 <= new_row < 8):
                    legal_moves.append((new_row, new_col))
            elif board[new_col][new_row] is None:
                print(f"capture unavailable at ({new_row},{new_col})")

        print(f"Legal moves: {legal_moves}")
        return legal_moves
