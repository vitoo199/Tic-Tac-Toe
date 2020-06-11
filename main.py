import random


class Cell():
    def __init__(self, id, val='', clickable=False):
        self.id = id
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


def empty_cells(board):
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
    [2, 5, 6],

    [0, 4, 8],
    [2, 4, 6],


]


def check_game_end(board):
    for comb in winning_combs:
        tmp = []
        for index in comb:
            if board[index].val != BOARD_DEFAULT_CHAR:
                tmp.append(board[index].val)
        if len(tmp) < 3:
            continue
        first = tmp[0]

        if len(list(filter(lambda e: e != first, tmp))) == 0:
            return first
    return False


def input_pos():
    row = input('Enter row: ')
    col = input('Enter column: ')

    return (int(row), int(col))


def deactivate_cell(board, *pos):
    board[to_1d_index(pos[0], pos[1])].clickable = False
    return board


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
        turn = AI

        empty_cell = empty_cells(board)[0]
        ai_row, ai_col = to_2d_index(empty_cell.id)
        board = mark_board(board, AI, ai_row, ai_col)
        board = deactivate_cell(board, ai_row, ai_col)

        turn = PLAYER

        print_matrix(board)
        if check_game_end(board):
            is_game_over = True


run()
