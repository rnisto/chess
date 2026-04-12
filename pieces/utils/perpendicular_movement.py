def PerpendicularMovement(board, pos):
    row, col = pos

    legal_moves = []
    potential_moves = []

    # loop over columns
    for i in range(-6, 6):
        new_col = col + i

        if new_col > 7 or new_col < 0: 
            next
        else:
            potential_moves.append((row,new_col))
        
        print(potential_moves)

    piece_locations = []
    for move in potential_moves:
        p_row, p_col  = move
        print(f"{p_row},{p_col}")
        if board[p_col][p_row] is not None:
            piece_locations.append(move)

    upper_bound = 7
    lower_bound = 0   
    for piece in piece_locations:
        p_row, p_col = piece

        if p_col > col and p_col < upper_bound:
            upper_bound = p_col
        
        if p_col < col and p_col > lower_bound:
            lower_bound = p_col
    
    for move in potential_moves:
        new_row, new_col  = move
        if lower_bound <= new_col <= upper_bound:
            legal_moves.append(move)
    
    return legal_moves



            


    return(legal_moves)
    