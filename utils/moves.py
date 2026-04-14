"""docstring"""

import utils.coordinates
import logging

class Squares:
    """A container for lists of squares"""
    def __init__(self, squares):
        self.squares = squares

    def algebraic(self):
        """A function that returns the algebraic coordinates of the squares"""
        algebraic_list = []
        for i in self.squares:
            algebraic_list.append(utils.coordinates.CoordToAlphabet(i))
        return algebraic_list
    
    def find_piece(self,board):
        """A function that returns the items / Pieces on the squares"""
        pieces = []
        for square in self.squares:
            row, col = square
            pieces.append(board[col][row])
        return pieces  

class Move:
    """A container for storing information about a move"""
    def __init__(self, start, end, p_moved, p_taken):
        self.start = start
        self.end = end
        self.p_moved = p_moved
        self.p_taken = p_taken
    
    def pgn(self):
        """A function that returns the pgn notation of the moves"""
        # pieces = self.start.find_piece(board)
        pieces_pgn = []
        for piece in p_moved:
            if piece is None:
                pieces_pgn.append("")
            elif piece.type == "p":
                pieces_pgn.append("")
            else: pieces_pgn.append((piece.type).upper())
        
        output = []
        for i in range(len(pieces_pgn)):
            output.append(f"{pieces_pgn[i]}{self.end.algebraic()[i]}")
        
        return output
    
class MoveList:
    """A container for lists of moves"""
    def __init__(self):
        self.moves = []

    def append(self,move:Move):
        self.moves.append(move)

def make_move(move:Move, board, move_list:MoveList):
    """docstring"""
    move_list.append(move)
    logging.debug(f"start:{move.start}, end:{move.end}, piece:{move.p_moved}")
    board[move.end[1]][move.end[0]] = move.p_moved
    board[move.start[1]][move.start[0]] = None
