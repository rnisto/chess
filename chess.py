# Example file showing a basic pygame "game loop".
import pygame
from pygame.locals import *
import logging
import datetime
from math import sqrt

import utils.fen
import utils.coordinates
import utils.render
import utils.moves
import utils.state

# Setup the log file. 
start_time = datetime.datetime.now()
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f"logs/{start_time.strftime("%Y%m%d-%H%M%S")}.log",
    encoding='utf-8', level=logging.DEBUG, 
    format="%(asctime)s %(message)s"
    )
logging.debug("Programme started")

# Setup pygame.
pygame.init()
framesize = (800,800)
SQUARE_SIZE = int(sqrt((framesize[0] * framesize[1]) / 64))
screen = pygame.display.set_mode(framesize)
clock = pygame.time.Clock()
running = True

# Define style. 
style = utils.state.Style()

# Definie initial params.
move_list = utils.moves.MoveList()
state = utils.state.GameState(move_list)

# Setting up the board.
starting_position_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
starting_position_fen = starting_position_fen.replace("/","")

starting_position = []
for char in starting_position_fen:
    if char.isnumeric():
        starting_position.extend([None] * int(char))
    else:
        starting_position.append(utils.fen.FenToPiece(char))
print(starting_position)

board = [['  ' for i in range(8)] for i in range(8)]

for col in range(8):
    for row in range(8):
        board[col][row] = starting_position[col*8 + row]

# Starting the game.
while running:
    # pygame.QUIT event means the user clicked X to close your window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Checking whether the user clicked on a square and moving pieces.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            state.clicked = utils.moves.Square(
                coords = utils.coordinates.PixelToGrid(mouse_pos,SQUARE_SIZE)
            )
            logging.debug(state.clicked.algebraic())

            if state.clicked is None:
                continue

            # If user clicked on a square, check if it has a piece and 
            # if so select it. This only runs if selected pieces is none
            # (i.e) the user still hasn't clicked on a piece.
            if state.start_square is None:
                logging.debug("user selecting a piece")
                if state.clicked.find_piece(board) is None:
                    continue  # click empty square → ignore
                elif (state.clicked.find_piece(board).colour 
                      == state.turn_colour):
                    state.start_square = state.clicked
                    state.legal_moves = (
                        state.start_square
                        .find_piece(board)
                        .get_legal_moves(board,state.start_square.coords)
                        )
                continue

            # If the user has selected a piece, then this click is to 
            # make a move. This checks whether the move is legal before
            # making it on the board.
            else:
                logging.debug("user selecting a move")                 
                # Ignore clicking same square.
                if state.clicked == state.start_square:
                    logging.debug("user selected start square. resetting move")
                    state.start_square = None
                    continue

                if state.clicked.coords in state.legal_moves:
                    logging.debug("Selected a legal move")
                    state.selected_move = utils.moves.Move(
                        start = state.start_square,
                        end = state.clicked,
                        p_moved = state.start_square.find_piece(board),
                        p_taken = state.clicked.find_piece(board)
                        )
                    state.selected_move.play(board, state.move_list)
                    state.new_turn(previous_pos=state.start_square,
                                   new_pos= state.clicked
                                   )
                else:
                    logging.debug("user selected an illegal move, starting over.")
                    state.reset_selection()
    

    # Fill the screen with a color to wipe away anything from last frame.
    screen.fill("purple")

    # Render the board.
    utils.render.RenderBoard(screen,framesize,SQUARE_SIZE,style)

    # Render square highlights.
    if state.previous_pos:
        utils.render.RenderSquare(state.previous_pos, SQUARE_SIZE,
                                  style.shade_col, screen
                                  )
    if state.new_pos:
        utils.render.RenderSquare(state.new_pos, SQUARE_SIZE,
                                  style.highlight_col, screen
                                  )
    if state.clicked:
        utils.render.RenderSquare(state.clicked, SQUARE_SIZE,
                                  style.highlight_col, screen
                                  )
    if state.legal_moves:
        for row, col in state.legal_moves:
            x, y = utils.coordinates.GridToPixel(row,col,SQUARE_SIZE)
            pygame.draw.circle(screen, style.highlight_col, (x, y),
                               SQUARE_SIZE / 10)    

    # Render the pieces.
    for rank in range(8):
     for file in range(8):
        piece = board[rank][file]
        if piece is not None:
            utils.render.RenderPiece(piece, rank, file, SQUARE_SIZE,
                                     style.font,screen
                                     )

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

logging.debug(move_list.pgn())
logging.debug("Programme ended")
pygame.quit()