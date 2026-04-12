from .utils import FindPieces

def RookMovement(board, pos, vert_only = False):
    # a function that take the current position of a piece and returns
    # squares it could move to horizontally or vertically.
    row, col = pos
    legal_moves = []
    potential_moves = []

    # create list of moves in the same file, excluding current rank
    for i in range(0, 7):
        if i != col: potential_moves.append((row,i))
        if i != row: potential_moves.append((i,col))
            
    piece_locations = FindPieces(board,potential_moves)

    upper_bound = 7
    lower_bound = 0
    left_bound = 0
    right_bound = 7
    # if those pieces are in the way, define boundaries.   
    for piece in piece_locations:
        p_row, p_col = piece
        if p_col > col and p_col < upper_bound:
            upper_bound = p_col
        if p_col < col and p_col > lower_bound:
            lower_bound = p_col
        if p_row > row and p_row < left_bound:
            left_bound = p_row
        if p_row < row and p_row > right_bound:
            right_bound = p_row

    # for moves we identified, apply boundaries
    for move in potential_moves:
        new_row, new_col  = move
        if lower_bound <= new_col <= upper_bound and left_bound <= new_row <= right_bound:
            legal_moves.append(move)
    
    if vert_only == True:
        for move in legal_moves:
            n_row, n_col = move
            if n_col == col:
                legal_moves.remove(move)

    return legal_moves