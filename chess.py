# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import *

from pieces import Pawn

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

dark_square_col = "#769656"
light_square_col = "#eeeed2"

my_font = pygame.font.SysFont('monospace', 100)

selected_piece = None
selected_pos = None
previous_pos = None
clicked = None
new_pos = None
legal_moves = None

turn_colour = "w"

SQUARE_SIZE = 100

def grid_to_pixel(row, col):
    x = row * SQUARE_SIZE + SQUARE_SIZE / 2
    y = col * SQUARE_SIZE + SQUARE_SIZE / 2
    return (x, y)

def pixel_to_grid(pos):
    x, y = pos
    row = int(x // SQUARE_SIZE)
    col = int(y // SQUARE_SIZE)
    return (row, col)

def render_piece(piece, row, col):
    y, x = grid_to_pixel(row,col)
    text_surface = my_font.render(piece.image, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center = (x,y))
    screen.blit(text_surface, text_rect)

piece_map = {
    'p': ('b', 'p', 'p'),
    'P': ('w', 'p', 'P'),
    'r': ('b', 'r', 'r'),
    'R': ('w', 'r', 'R'),
    'n': ('b', 'n', 'n'),
    'N': ('w', 'n', 'N'),
    'b': ('b', 'b', 'b'),
    'B': ('w', 'b', 'B'),
    'q': ('b', 'q', 'q'),
    'Q': ('w', 'q', 'Q'),
    'k': ('b', 'k', 'k'),
    'K': ('w', 'k', 'K'),
}

def fen_to_piece(char):
    colour, type, image = piece_map[char]

    if type == "p":
        return Pawn(colour, type, image)
    return None


def get_pos(mouse_pos):
    row, col = pixel_to_grid(mouse_pos)
    print(row, col)
    if 0 <= row < 8 and 0 <= col < 8:
        return (row,col)
    return None

starting_position_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
starting_position_fen = starting_position_fen.replace("/","")

starting_position = []
for char in starting_position_fen:
    if char.isnumeric():
        starting_position.extend([None] * int(char))
    else:
        starting_position.append(fen_to_piece(char))
print(starting_position)

board = [['  ' for i in range(8)] for i in range(8)]

for col in range(8):
    for row in range(8):
        board[col][row] = starting_position[col*8 + row]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            clicked = get_pos(mouse_pos)

            if clicked is None:
                continue

            row, col = clicked
            piece = board[col][row]

            # SELECT PIECE
            if selected_piece is None:
                if piece is None:
                    continue  # click empty square → ignore
                elif piece.colour == turn_colour:
                    selected_piece = piece
                    selected_pos = (row, col)
                    legal_moves = piece.get_legal_moves(board,selected_pos)
                continue

            # MOVE PIECE
            else:                
                start_row, start_col = selected_pos
                
                # ignore clicking same square
                if (row, col) == (start_row, start_col):
                    selected_piece = None
                    selected_pos = None
                    continue

                if clicked in legal_moves:
                    board[col][row] = selected_piece
                    board[start_col][start_row] = None

                    previous_pos = selected_pos
                    new_pos = (row,col)
                    selected_piece = None
                    selected_pos = None
                    legal_moves = None
                    
                    turn_colour = "b" if turn_colour == "w" else "w"
                else:
                    selected_pos = None
                    selected_piece = None
                    legal_moves = None
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # render the board
    for y in range(0,800,100):
        for x in range(0,800,100):
            rect = pygame.Rect(x, y, 100, 100)
            if x/100%2 == y/100%2:
                colour = dark_square_col
            else:
                colour = light_square_col
            pygame.draw.rect(screen, colour, rect)

    if previous_pos:
        row, col = previous_pos
        x, y = grid_to_pixel(row,col)
        highlight_rect = pygame.Rect(x-50, y-50, 100, 100)
        pygame.draw.rect(screen, "#eaf59a", highlight_rect)    

    if new_pos:
        row, col = new_pos
        x, y = grid_to_pixel(row,col)
        highlight_rect = pygame.Rect(x-50, y-50, 100, 100)
        pygame.draw.rect(screen, "#baca44", highlight_rect)         

    if clicked:
        row, col = clicked
        x, y = grid_to_pixel(row,col)
        highlight_rect = pygame.Rect(x-50, y-50, 100, 100)
        pygame.draw.rect(screen, "#baca44", highlight_rect)

    if legal_moves:
        for row, col in legal_moves:
            x, y = grid_to_pixel(row,col)
            pygame.draw.circle(screen, "#baca44", (x, y), 10)    


    # render the pieces
    for rank in range(8):
     for file in range(8):
        piece = board[rank][file]

        if piece is not None:
            render_piece(piece, rank, file)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()