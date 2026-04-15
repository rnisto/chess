"""docstring"""

from __future__ import annotations

import utils.coordinates
import logging

class SquareList:
    """A container for lists of squares"""
    def __init__(self, squares):
        self.squares = squares

    def algebraic_all(self):
        """A function that returns the algebraic coordinates of the squares"""
        algebraic_list = []
        for i in self.squares:
            algebraic_list.append(utils.coordinates.CoordToAlphabet(i))
        return algebraic_list
    
    def find_piece_all(self,board):
        """A function that returns the items / Pieces on the squares"""
        pieces = []
        for square in self.squares:
            row, col = square
            pieces.append(board[col][row])
        return pieces  

class Square:
    """A container for a square"""
    def __init__(self, coords):
        self.coords = coords

    def algebraic(self):
        """A function that returns the algebraic coordinates of the square"""
        return utils.coordinates.CoordToAlphabet(self.coords)
    
    def find_piece(self,board):
        """A function that returns the items / Pieces on the squares"""
        row, col = self.coords
        return board[col][row]

class Move:
    """A container for storing information about a move"""
    def __init__(self, start, end, p_moved, p_taken):
        self.start = start
        self.end = end
        self.p_moved = p_moved
        self.p_taken = p_taken
    
    def algebraic(self):
        """A function that returns the pgn notation of the moves
        This function is incomplete. It doesn't cover captures, or that other
        edge cases such as when to include the rank / file of a piece. 
        """
        if self.p_moved is None:
            piece = ""
        elif self.p_moved.type == "p":
            piece = ""
        else: piece = self.p_moved.type.upper()
    
        return f"{piece}{self.end.algebraic()}"
    
    def play(self, board, move_list:MoveList):
        """docstring"""
        move_list.append(self)
        board[self.end.coords[1]][self.end.coords[0]] = self.p_moved
        board[self.start.coords[1]][self.start.coords[0]] = None        
    
class MoveList:
    """A container for lists of moves"""
    def __init__(self):
        self.moves = []

    def append(self,move:Move):
        """A function append moves to the movelist"""
        self.moves.append(move)

    def pgn(self):
        """A function that returns the pgn notation of the moves"""
        pieces_pgn = []
        for move in self.moves:
            if move.p_moved is None:
                pieces_pgn.append("")
            elif move.p_moved.type == "p":
                pieces_pgn.append("")
            else: pieces_pgn.append((move.p_moved.type).upper())
        
        output = []
        for i in range(len(pieces_pgn)):
            output.append(f"{pieces_pgn[i]}{self.moves[i].end.algebraic()}")
        
        return output
