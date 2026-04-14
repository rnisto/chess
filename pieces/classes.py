"""Defines the classes for each of the Chess pieces"""

import movement
from math import sqrt

class Piece:
    """An object with defined movement rules around the board"""
    def __init__(self, colour, type, image):
        self.colour = colour
        self.type = type
        self.image = image

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        return []

class Pawn(Piece):
    """A Piece that can generally only move forward a single square per
    per turn. It can take pieces diagonally one space ahead of it"""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        # use self, not board lookup
        direction = 1 if self.colour == "b" else -1
        
        # pawns can move up to 2 squares
        if (self.colour == "w" and col == 6) or (self.colour == "b" and col == 1):
            distance = 2 
        else: distance = 1

        legal_moves = []

        vertical_moves = movement.RookMovement(board,pos, vert_only= True)
        for move in vertical_moves:
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

class Rook(Piece):
    """A Piece that can move to any square horizontally or diagonally."""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []

        for move in movement.RookMovement(board,pos):
            move_row, move_col = move
            if board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        print(f"Legal moves: {legal_moves}")
        return legal_moves

class Bishop(Piece):
    """A Piece which can move diagonally in any direction"""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []

        for move in movement.BishopMovement(board,pos):
            move_row, move_col = move
            if board[move_col][move_row] is not None:
                if board[move_col][move_row].colour != self.colour:
                    legal_moves.append(move)
                else: continue
            else: 
                legal_moves.append(move)

        print(f"Legal moves: {legal_moves}")
        return legal_moves

class Queen(Piece):
    """A Piece that can move to any square horizontally or diagonally."""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []
        potential_moves = (movement.BishopMovement(board,pos) 
                        + movement.RookMovement(board,pos)
                        )
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

class King(Piece):
    """A Piece that can move one square in any direction, or 'castle'"""
    def __init__(self, colour, type, image):
        super().__init__(colour, type, image)

    def get_legal_moves(self, board, pos):
        """Returns the legal moves of the Piece in the given position"""
        row, col = pos

        legal_moves = []
        potential_moves = (movement.BishopMovement(board,pos) 
                        + movement.RookMovement(board,pos)
                        )
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
