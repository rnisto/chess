"""A set of functions to determine the movement of pieces"""
import logging
from math import sqrt

def FindPieces(board,moves):
    """Finds pieces on squares given in move list"""
    locations = []
    for move in moves:
        p_row, p_col  = move
        if board[p_col][p_row] is not None:
            locations.append(move)
        else:
            continue
    return locations  

def RookMovement(board, pos, vert_only = False):
    # A function that take the current position of a piece and returns
    # squares it could move to horizontally or vertically.
    row, col = pos
    legal_moves = []
    potential_moves = []

    # Create list of moves in the same file or same rank.
    for i in range(0, 8):
        if i != col: potential_moves.append((row,i))
        if i != row: potential_moves.append((i,col))

    logging.debug(
        f"Found {len(potential_moves)} potential moves: {potential_moves}"
        )
    
    # Identify Pieces in the potential move locations.
    piece_locations = FindPieces(board,potential_moves)
    logging.debug(f"Found pieces at these locations: {piece_locations}")
    
    # Define initial boundaries.
    n_bound = 0
    s_bound = 7
    e_bound = 7
    w_bound = 0

    # If those pieces are in the way, redefine boundaries.   
    for piece in piece_locations:
        p_row, p_col = piece
        if p_col < col and p_col > n_bound:
            n_bound = p_col
        if p_col > col and p_col < s_bound:
            s_bound = p_col
        if p_row > row and p_row < e_bound:
            e_bound = p_row
        if p_row < row and p_row > w_bound:
            w_bound = p_row
    logging.debug(f"Boundaries defined at n:{n_bound}, s:{s_bound}, w: {w_bound}, e: {e_bound}")

    # For moves identified, apply boundaries.
    for move in potential_moves:
        new_row, new_col  = move
        if ((n_bound <= new_col <= s_bound) 
            and (w_bound <= new_row <= e_bound)):
                legal_moves.append(move)
    
    # Limit horizontal movement (for pawns).
    if vert_only == True:
        for move in legal_moves:
            n_row, n_col = move
            if n_col == col:
                legal_moves.remove(move)

    return legal_moves

def KnightMovement(board, pos):
    # A function that take the current position of a piece and returns
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

    logging.debug(
        f"Found {len(legal_moves)} potential moves: {legal_moves}"
        )
    
    return legal_moves

def BishopMovement(board, pos):
    # A function that take the current position of a piece and returns
    # squares it could move to diagonally.
    row, col = pos
    legal_moves = []
    potential_moves = []

    # Create list of moves on the diagonals
    for i in range(-7,8):
       for j in [1,-1]:
            new_pos = (row + i, col + i*j)
            if max(new_pos) < 8 and min(new_pos) >= 0:
                potential_moves.append(new_pos)
    potential_moves = [x for x in potential_moves if x != pos]

    logging.debug(
        f"Found {len(potential_moves)} potential moves: {potential_moves}"
        )

    # Finding pieces located on the potential movement squares.
    piece_locations = FindPieces(board,potential_moves)
    logging.debug(f"Found pieces at these locations: {piece_locations}")
    
    # Define initial boundaries.
    nw_bound = 7
    ne_bound = 7
    sw_bound = 7
    se_bound = 7

    # If those pieces are in the way, narrow boundaries.   
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

    # For moves identified, apply boundaries.
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

