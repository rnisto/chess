from .utils import FindPieces
import logging
from math import sqrt

def BishopMovement(board, pos, vert_only = False):
    # a function that take the current position of a piece and returns
    # squares it could move to diagonally.
    row, col = pos
    legal_moves = []
    potential_moves = []

    # create list of moves on the diagonals
    for i in range(-7,8):
       for j in [1,-1]:
            new_pos = (row + i, col + i*j)
            if max(new_pos) < 8 and min(new_pos) >= 0:
                potential_moves.append(new_pos)
    potential_moves = [x for x in potential_moves if x != pos]

    logging.debug(f"Found {len(potential_moves)} potential moves: {potential_moves}")
    piece_locations = FindPieces(board,potential_moves)

    logging.debug(f"Found pieces at these locations: {piece_locations}")
    
    nw_bound = 7
    ne_bound = 7
    sw_bound = 7
    se_bound = 7

    # if those pieces are in the way, define boundaries.   
    for piece in piece_locations:
        p_row, p_col = piece
        dist = int(sqrt((p_row - row)**2 + (p_col - col)**2))
        
        if p_col > col and p_row > row:
            if dist < nw_bound:
                nw_bound = dist
        elif p_col > col and p_row < row:
            if dist < ne_bound:
                ne_bound = dist   
        elif p_col < col and p_row > row:
            if dist < sw_bound:
                sw_bound = dist   
        elif p_col < col and p_row < row:
            if dist < se_bound:
                se_bound = dist                  
    
    logging.debug(f"Boundaries defined at u:{nw_bound}, l:{ne_bound}, left: {sw_bound}, right: {se_bound}")

    # for moves we identified, apply boundaries
    for move in potential_moves:
        new_row, new_col  = move
        dist = int(sqrt((new_row - row)**2 + (new_col - col)**2))
        if (new_col > col and new_row > row) and dist <= nw_bound:
            legal_moves.append(move)
        elif (new_col > col and new_row < row) and dist <= ne_bound:
            legal_moves.append(move)
        elif (new_col < col and new_row > row) and dist <= sw_bound:
            legal_moves.append(move)
        elif (new_col < col and new_row < row) and dist <= se_bound:
            legal_moves.append(move)

    return legal_moves