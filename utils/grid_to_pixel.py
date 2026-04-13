def GridToPixel(row, col, square_size):
    x = row * square_size + square_size / 2
    y = col * square_size + square_size / 2
    return (x, y)