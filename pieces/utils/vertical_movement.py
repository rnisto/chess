from .utils import FindPieces

def VerticalMovement(board, pos):
    # a function that take the current position of a piece and returns squares it could moves to within the same file.
    row, col = pos

    legal_moves = []
    potential_moves = []

    # create list of moves in the same file, excluding current rank
    for new_col in range(0, 7):
        if new_col != col: potential_moves.append((row,new_col))

    piece_locations = FindPieces(board,potential_moves)

    upper_bound = 7
    lower_bound = 0
    # if those pieces are in the way, define boundaries.   
    for piece in piece_locations:
        p_row, p_col = piece
        if p_col > col and p_col < upper_bound:
            upper_bound = p_col
        if p_col < col and p_col > lower_bound:
            lower_bound = p_col
    
    # for moves we identified, apply boundaries
    for move in potential_moves:
        new_row, new_col  = move
        if lower_bound <= new_col <= upper_bound:
            legal_moves.append(move)
    
    return legal_moves