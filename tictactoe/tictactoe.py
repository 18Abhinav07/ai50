"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    Based on a count of cells occupied by  x and o , assumed that
    x has a first chance in the beginning of the board.
    """
    count_x = 0
    count_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1

    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    current_board = copy.deepcopy(board)
    if player(current_board) == X:
        current_board[i][j] = X
    else:
        current_board[i][j] = O

    return current_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Classic three cases of winning is possible:
    horizontal
    vertical
    left diagonal
    right diagonal
    """
    winner_player = None
    # Horizontal test
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            winner_player = board[i][0]

    # Vertical test
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            winner_player = board[0][i]

    # Diagonal test
    if (board[1][1] == board[0][0] == board[2][2] and board[1][1] != EMPTY) or (
            board[1][1] == board[0][2] == board[2][0] and board[1][1] != EMPTY
    ):
        winner_player = board[1][1]
    return winner_player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(temp_board):
        best_move = None

        if terminal(temp_board):
            return utility(temp_board), None

        max_value_obtained = -math.inf

        for action in actions(temp_board):
            action_score = min_value(result(temp_board, action))
            if action_score[0] > max_value_obtained:
                max_value_obtained = action_score[0]
                best_move = action
                if max_value_obtained == 1:
                    break

        return max_value_obtained, best_move

    def min_value(temp_board):
        best_move = None

        if terminal(temp_board):
            return utility(temp_board), None

        min_value_obtained = math.inf

        for action in actions(temp_board):
            action_score = max_value(result(temp_board, action))
            if action_score[0] < min_value_obtained:
                min_value_obtained = action_score[0]
                best_move = action
                if min_value_obtained == -1:
                    break

        return min_value_obtained, best_move

    current_player = player(board)

    if current_player == X:
        score, bestMove = max_value(board)
    else:
        score, bestMove = min_value(board)
    return bestMove
