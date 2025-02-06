import math

class Board:
    def __init__(self):
        self.player = 0 # 0 if white, 1 if black

    def is_player_turn(self):
        pass

    def execute_move(self, move):
        pass

    def get_legal_moves(self): # returns a list
        pass

    def evaluate_curr_board(self, player): # Positive score if player is winning and negative if player is losing
        return math.random(0, 10)
    
    def is_game_over(self):
        pass

    def copy(self):
        pass