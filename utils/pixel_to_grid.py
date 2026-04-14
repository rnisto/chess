def PixelToGrid(pos,square_size):
    """Takes a pixel position and returns the board position""" 
    x, y = pos
    row = int(x // square_size)
    col = int(y // square_size)
    return (row, col)