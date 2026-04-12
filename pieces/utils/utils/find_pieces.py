def FindPieces(board,moves):
# find pieces on potential movement squares
    locations = []
    for move in moves:
        p_row, p_col  = move
        if board[p_col][p_row] is not None:
            locations.append(move)
        else:
            continue
    return locations  