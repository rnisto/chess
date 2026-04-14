def GridToPixel(row, col, square_size):
    """This function takes a board / grid postion and returns the pixel
    position of the centre of the square"""
    x = row * square_size + square_size / 2
    y = col * square_size + square_size / 2
    return (x, y)