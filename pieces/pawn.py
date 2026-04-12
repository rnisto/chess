from .piece import Piece

class Pawn(Piece):
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        row, col = pos

        # use self, not board lookup
        direction = 1 if self.colour == "b" else -1
        print(self.colour)
        
        # pawns can move up to 2 squares
        if (self.colour == "w" and col == 6) or (self.colour == "b" and col == 1):
            distance = 2 
        else: distance = 1

        legal_moves = []

        # pawns can move forward but cannot move onto other peices
        for i in range(distance):
            new_col = col + (i + 1) * direction
            if board[new_col][row] is None and (0 <= new_col < 8):
                legal_moves.append((row, new_col))
            elif board[new_col][row] is not None:
              print("Pawn is blocked")

        # pawns can capture diagonally   
        for i in [-1,1]:
            new_col = col + direction
            new_row = row + i
            
            if board[new_col][new_row] is not None:
                print(f"capture available at ({new_row},{new_col})")
                if (board[new_col][new_row].colour is not self.colour) and (0 <= new_col < 8 and 0 <= new_row < 8):
                    legal_moves.append((new_row, new_col))
            elif board[new_col][new_row] is None:
                print(f"capture unavailable at ({new_row},{new_col})")

        print(f"Legal moves: {legal_moves}")
        return legal_moves
