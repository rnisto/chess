def CoordToAlphabet(coord:tuple):
    """This function converts row, col coords into algebraic chess notation"""
    row, col = coord
    start = ord("a") - 1

    col_new = abs(col - 8)
    row_new = chr(start + row + 1)

    return(f"{row_new}{col_new}")