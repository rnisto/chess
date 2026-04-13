def PixelToGrid(pos,square_size):
    x, y = pos
    row = int(x // square_size)
    col = int(y // square_size)
    return (row, col)