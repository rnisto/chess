from .grid_to_pixel import GridToPixel
import pygame
from pygame.locals import *

def RenderSquare(pos, square_size, colour, screen):
    row, col = pos
    x, y = GridToPixel(row,col,square_size)
    rect = pygame.Rect(x-(square_size/2), y-(square_size/2), square_size, square_size)
    pygame.draw.rect(screen, colour, rect)