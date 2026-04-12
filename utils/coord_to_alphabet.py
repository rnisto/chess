def CoordToAlphabet(coord:tuple):
    row, col = coord
    
    start = ord("a") - 1

    col_new = abs(col - 8)
    row_new = chr(start + row + 1)

    return(f"{row_new}{col_new}")