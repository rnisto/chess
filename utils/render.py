"""docstring"""

import pygame
from pygame.locals import *
import utils.coordinates

def RenderPiece(piece, row, col, square_size, font, screen):
    """Renders the given piece at the specificied board location"""
    y, x = utils.coordinates.GridToPixel(row,col,square_size)
    text_surface = font.render(piece.image, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center = (x,y))
    screen.blit(text_surface, text_rect)

def RenderSquare(pos, square_size, colour, screen):
    """Renders a square in the given pixel position on the screen"""
    row, col = pos
    x, y = utils.coordinates.GridToPixel(row,col,square_size)
    rect = pygame.Rect(x-(square_size/2), y-(square_size/2), square_size, square_size)
    pygame.draw.rect(screen, colour, rect)