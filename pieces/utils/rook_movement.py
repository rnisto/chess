from .utils import FindPieces
import logging

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
        if (n_bound <= new_col <= s_bound) 
            and (w_bound <= new_row <= e_bound):
                legal_moves.append(move)
    
    # Limit horizontal movement (for pawns).
    if vert_only == True:
        for move in legal_moves:
            n_row, n_col = move
            if n_col == col:
                legal_moves.remove(move)

    return legal_moves