"""docstring"""
import utils.moves
import pygame

class GameState:
    """A class for holding game state variables"""
    def __init__(self, move_list):
        self.clicked:utils.moves.Square = None
        self.previous_pos:utils.moves.Square = None
        self.new_pos:utils.moves.Square = None
        self.start_square:utils.moves.Square = None
        self.legal_moves:utils.moves.MoveList = None
        self.turn_colour:str = "w"
        self.move_list:utils.moves.MoveList = move_list
    
    def new_turn(self,previous_pos:utils.moves.Square, new_pos:utils.moves.Square):
        self.previous_pos = previous_pos
        self.new_pos = new_pos

        self.start_square = None
        self.legal_moves = None
        self.clicked = None

        self.turn_colour = "b" if self.turn_colour == "w" else "w"

    def reset_selection(self):
        self.start_square = None
        self.legal_moves = None

class Style:
    """A class for holding style variables"""
    def __init__(self):
        self.dark_col:str = "#769656"
        self.light_col:str = "#eeeed2"
        self.highlight_col:str = "#baca44"
        self.shade_col:str = "#eaf59a"
        self.font = pygame.font.SysFont('monospace', 100)