from .utils import FindPieces
import logging
from math import sqrt

def KnightMovement(board, pos):
    # a function that take the current position of a piece and returns
    # squares a knight's move away.
    row, col = pos
    legal_moves = []
    for i in range(row - 2, row + 3):
        for j in range(col - 2, col + 3):
            move = (i, j)
            logging.debug(f"Testing: {move}")
            dist = sqrt((i-row)**2 + (j-col)**2)
            if dist == sqrt(5) and max(move) < 8 and min(move) >= 0:
                legal_moves.append(move)
            else: continue

    logging.debug(f"Found {len(legal_moves)} potential moves: {legal_moves}")
    
    return legal_moves