# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import *
import logging
import datetime
from math import sqrt

from utils import CoordToAlphabet, GridToPixel, PixelToGrid, RenderPiece, FenToPiece, GetPos, RenderSquare

# setup log
start_time = datetime.datetime.now()
logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"logs/{start_time.strftime("%Y%m%d-%H%M%S")}.log", encoding='utf-8', level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Programme started")

# pygame setup
pygame.init()
framesize = (800,800)
SQUARE_SIZE = int(sqrt((framesize[0] * framesize[1]) / 64))
screen = pygame.display.set_mode(framesize)
clock = pygame.time.Clock()
running = True

# set style
dark_square_col = "#769656"
light_square_col = "#eeeed2"
highlight_col = "#baca44"
shade_col = "#eaf59a"
my_font = pygame.font.SysFont('monospace', 100)

# initial params
selected_piece = None
selected_pos = None
previous_pos = None
clicked = None
new_pos = None
legal_moves = None
turn_colour = "w"

# setting up board
starting_position_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
starting_position_fen = starting_position_fen.replace("/","")

starting_position = []
for char in starting_position_fen:
    if char.isnumeric():
        starting_position.extend([None] * int(char))
    else:
        starting_position.append(FenToPiece(char))
print(starting_position)

board = [['  ' for i in range(8)] for i in range(8)]

for col in range(8):
    for row in range(8):
        board[col][row] = starting_position[col*8 + row]

# starting game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            clicked = GetPos(mouse_pos,SQUARE_SIZE)
            logging.debug(CoordToAlphabet(clicked))

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
    for y in range(0,framesize[0],SQUARE_SIZE):
        for x in range(0,framesize[1],SQUARE_SIZE):
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            if x/SQUARE_SIZE%2 == y/SQUARE_SIZE%2:
                colour = dark_square_col
            else:
                colour = light_square_col
            pygame.draw.rect(screen, colour, rect)

    # render highlights
    if previous_pos:
        RenderSquare(previous_pos, SQUARE_SIZE, shade_col, screen)  

    if new_pos:
        RenderSquare(new_pos, SQUARE_SIZE, highlight_col, screen)   

    if clicked:
        RenderSquare(clicked, SQUARE_SIZE, highlight_col, screen)

    if legal_moves:
        for row, col in legal_moves:
            x, y = GridToPixel(row,col,SQUARE_SIZE)
            pygame.draw.circle(screen, highlight_col, (x, y), SQUARE_SIZE / 10)    

    # render the pieces
    for rank in range(8):
     for file in range(8):
        piece = board[rank][file]
        if piece is not None:
            RenderPiece(piece, rank, file, SQUARE_SIZE, my_font, screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

logging.debug("Programme ended")
pygame.quit()