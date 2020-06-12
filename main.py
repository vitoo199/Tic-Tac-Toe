import random
import copy


class Cell():
    def __init__(self, _id, val='', clickable=False):
        self.id = _id
        self.val = val
        self.clickable = clickable


ROW = 3
COLUMN = 3
PLAYER = 'O'
AI = 'X'
BOARD_DEFAULT_CHAR = '#'

# 3
# 3 / 3 = 1
# 3 % 3
turn = PLAYER


def to_2d_index(index):
    if index == 0:
        return (0, 0)
    return (int(index/ROW), COLUMN % index - 1)


def to_1d_index(i, j):
    row = i * ROW
    if j != 0:
        col = COLUMN * COLUMN % j
        return row + col + 1

    else:
        col = 0
        return row


def get_empty_cells(board):
    return [cell for cell in board if cell.clickable]


def print_matrix(matrix):
    for i in range(ROW):
        tmp = ''
        for j in range(COLUMN):
            tmp += matrix[to_1d_index(i, j)].val
        print(' '.join(tmp))
        tmp = ''


winning_combs = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6],


]


def check_game_end(board):
    for comb in winning_combs:
        for index in range(len(comb) - 2):
            if board[comb[index]].val != BOARD_DEFAULT_CHAR and board[comb[index]].val == board[comb[index + 1]].val and board[comb[index]].val == board[comb[index + 2]].val:
                return board[comb[index]].val
    return False


def input_pos():
    row = input('Enter row: ')
    col = input('Enter column: ')

    return (int(row), int(col))


def opposite_turn(turn):
    return PLAYER if turn == AI else AI


def is_draw(board):
    return get_empty_cells(board) == 0 and not check_game_end(board)


def deactivate_cell(board, *pos):
    board[to_1d_index(pos[0], pos[1])].clickable = False
    return board


def minimax(pos, maximazingPlayer, best_move=None):

    game_end_result = check_game_end(pos)
    if game_end_result == PLAYER:
        return [-1, best_move]
    elif game_end_result == AI:
        return [1, best_move]
    if is_draw(pos):
        return [0, best_move]
    if maximazingPlayer:
        maxEval = -9999
        empty_cells = get_empty_cells(pos)
        current_best_move = None
        for empty_cell in empty_cells:
            pos[empty_cell.id].val = PLAYER
            pos[empty_cell.id].clickable = False
            _eval, move = minimax(
                copy.deepcopy(pos),  False, empty_cell.id)
            print(_eval, move)
            if _eval > maxEval:
                maxEval = _eval
                current_best_move = move

        return [maxEval, current_best_move]
    else:
        minEval = 9999
        empty_cells = get_empty_cells(pos)
        current_best_move = None
        for empty_cell in empty_cells:
            pos[empty_cell.id].val = AI
            pos[empty_cell.id].clickable = False
            _eval, move = minimax(
                  copy.deepcopy(pos), True, empty_cell.id)
            if _eval < minEval:
                minEval = _eval
                current_best_move = move

        return [minEval, current_best_move]


def mark_board(board, mark, *pos):
    index = to_1d_index(pos[0], pos[1])
    board[index].val = mark
    return board


def run():
    board = [
        Cell(0, BOARD_DEFAULT_CHAR, True),
        Cell(1, BOARD_DEFAULT_CHAR, True),
        Cell(2, BOARD_DEFAULT_CHAR, True),

        Cell(3, BOARD_DEFAULT_CHAR, True),
        Cell(4, BOARD_DEFAULT_CHAR, True),
        Cell(5, BOARD_DEFAULT_CHAR, True),

        Cell(6, BOARD_DEFAULT_CHAR, True),
        Cell(7, BOARD_DEFAULT_CHAR, True),
        Cell(8, BOARD_DEFAULT_CHAR, True),
    ]
    is_game_over = False
    print_matrix(board)

    while is_game_over == False:
        while True:
            row, col = input_pos()
            i_cell = board[to_1d_index(row, col)]
            if i_cell.clickable:
                board = mark_board(board, PLAYER, row, col)
                board = deactivate_cell(board, row, col)
                break
            else:
                print('Already taken! Pick another one!')
        if check_game_end(board):
            print(f'GAME ENDED AFTER USER!')
            is_game_over = True
            break

        _, i = minimax(copy.deepcopy(board), True)
        print(_)
        board[i].val = AI
        board[i].clickable = False

        turn = PLAYER

        print_matrix(board)
        if check_game_end(board):
            print(f'GAME ENDED!')
            is_game_over = True
            break


run()
