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
    row, col = pos.coords
    x, y = utils.coordinates.GridToPixel(row,col,square_size)
    rect = pygame.Rect(x-(square_size/2), y-(square_size/2), 
                       square_size, square_size)
    pygame.draw.rect(screen, colour, rect)

def RenderBoard(screen,framesize,square_size,style):
    for y in range(0,framesize[0],square_size):
        for x in range(0,framesize[1],square_size):
            rect = pygame.Rect(x, y, square_size, square_size)
            if x/square_size%2 == y/square_size%2:
                colour = style.light_col
            else:
                colour = style.dark_col
            pygame.draw.rect(screen, colour, rect) 

def RenderLegalMoves(moves, board, screen, square_size, style, state):
    for row, col in moves:
        if row/square_size%2 == col/square_size%2:
            colour = style.light_col
        else:
            colour = style.dark_col
        if board[col][row] is None:
            x, y = utils.coordinates.GridToPixel(row,col,square_size)
            pygame.draw.circle(screen, style.highlight_col, (x, y),
                                square_size / 10)
        elif (row,col) == state.new_pos.coords:
            RenderSquare(utils.moves.Square((row,col)), square_size,
                         style.highlight_col, screen
                         )
            x, y = utils.coordinates.GridToPixel(row,col,square_size)
            pygame.draw.circle(screen, style.shade_col, (x, y),
                                square_size / 2)
        else: 
            RenderSquare(utils.moves.Square((row,col)), square_size,
                         style.highlight_col, screen
                         )
            x, y = utils.coordinates.GridToPixel(row,col,square_size)
            pygame.draw.circle(screen, colour, (x, y),
                                square_size / 2)
         
