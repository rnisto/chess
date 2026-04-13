from .pixel_to_grid import PixelToGrid

def GetPos(mouse_pos, square_size):
    row, col = PixelToGrid(mouse_pos,square_size)
    print(row, col)
    if 0 <= row < 8 and 0 <= col < 8:
        return (row,col)
    return None