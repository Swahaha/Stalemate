import math

def find_best_move_non_recursive(board):
    """non-recursive"""
    # create copy of board
    temp_board = board.copy()

    best_score, best_move = -float('inf'), None

    for move in board.get_legal_moves():
        temp_board.execute_move()
        score = temp_board.evaluate_curr_board()
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def find_best_move(board, player, depth = 3, curr_depth = 0):
    """use minimax alg"""

    best_score, best_move = -float('inf'), None
    
    if board.is_player_turn(player): # If it is our turn run MAX
        for move in board.get_legal_moves(player):
            temp_board = board.copy()
            temp_board.execute_move(move)

            if curr_depth < depth:
                (score, best_move) = find_best_move(temp_board, player + 1 % 2, depth, curr_depth + 1)

            score = temp_board.evaluate_curr_board()
            if score < best_score:
                best_score, best_move = score, move

    else: # If it is their turn, run min.
        for move in board.get_legal_moves(player):
            temp_board = board.copy()
            temp_board.execute_move(move)

            if curr_depth < depth:
                (score, best_move) = find_best_move(temp_board, player + 1 % 2, depth, curr_depth + 1)

            score = temp_board.evaluate_curr_board()
            if score < best_score:
                best_score, best_move = score, move
    
    return (score, best_move)
