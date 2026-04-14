from .grid_to_pixel import GridToPixel

def RenderPiece(piece, row, col, square_size, font, screen):
    """Renders the given piece at the specificied board location"""
    y, x = GridToPixel(row,col,square_size)
    text_surface = font.render(piece.image, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center = (x,y))
    screen.blit(text_surface, text_rect)