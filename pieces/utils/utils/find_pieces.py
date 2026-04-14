def FindPieces(board,moves):
    """ Finds pieces on squares given in move list"""
    locations = []
    for move in moves:
        p_row, p_col  = move
        if board[p_col][p_row] is not None:
            locations.append(move)
        else:
            continue
    return locations  