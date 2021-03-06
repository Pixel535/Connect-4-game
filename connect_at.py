import copy
import random
import math

# Set the min-max IDs, and pseudo infinity constants
MIN = -1
MAX = 1
INFINITY_POSITIVE = math.inf
INFINITY_NEGATIVE = -math.inf


# This class contains a move and the respective value earned for that move
class Move:

    def __init__(self, move=0, value=0):
        self.move = move
        self.value = value


# Choose a move given a game and a search depth
def choose_move(connect, depth):
    print('Thinking...')
    move_result = False
    # Search for a move until a valid one is found
    while move_result is False:
        move_result = minmax_ab_pruning(connect, depth, MAX, 0, -math.inf, math.inf).move
    return move_result


def minmax_ab_pruning(state, depth, min_or_max, last_move, alpha, beta):
    current_score = state.get_score_for_ai()
    current_is_board_full = state.is_board_full()
    if current_score != 0 or current_is_board_full or depth == 0:
        return Move(last_move, current_score)
    best_score = INFINITY_NEGATIVE * min_or_max
    best_max_move = -1
    moves = random.sample(range(0, state.board_size_y + 1), state.board_size_x)
    for slot in moves:
        neighbor = copy.deepcopy(state)
        move_outcome = neighbor.play_move(slot)
        if move_outcome:
            best = minmax_ab_pruning(neighbor, depth - 1, min_or_max * -1, slot, alpha, beta)
            if (min_or_max == MAX and best.value > best_score) or (min_or_max == MIN and best.value < best_score):
                best_score = best.value
                best_max_move = best.move
                if best_score >= alpha:
                    alpha = best_score
                if best_score <= beta:
                    beta = best_score
            if alpha >= beta:
                break
    return Move(best_max_move, best_score)
