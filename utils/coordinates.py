"""A set of functions to manipulate / convert between coordinate systems"""

def CoordToAlphabet(coord:tuple):
    """This function converts row, col coords into algebraic chess notation"""
    row, col = coord
    start = ord("a") - 1

    col_new = abs(col - 8)
    row_new = chr(start + row + 1)

    return(f"{row_new}{col_new}")

def GridToPixel(row, col, square_size):
    """This function takes a board / grid postion and returns the pixel
    position of the centre of the square"""
    x = row * square_size + square_size / 2
    y = col * square_size + square_size / 2
    return (x, y)

def PixelToGrid(pos,square_size):
    """Takes a pixel position and returns the board position""" 
    x, y = pos
    row = int(x // square_size)
    col = int(y // square_size)
    return (row, col)