from Cell import Cell
import consts
import copy


class Game():
    def __init__(self, board):
        self.board = board
        self.winning_combs = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [2, 4, 6],


        ]

    def opposite_turn(self, turn):
        return consts.PLAYER if turn == consts.AI else consts.AI

    def is_draw(self, board):
        return board.get_empty_cells() == 0 and not self.check_game_end(board)

    def input_pos(self):
        row = input('Enter row: ')
        col = input('Enter column: ')

        return (int(row), int(col))

    def to_2d_index(self, index):
        if index == 0:
            return (0, 0)
        return (int(index/consts.ROW), index % consts.COLUMN)

    def check_game_end(self, board):
        for comb in self.winning_combs:
            for index in range(len(comb) - 2):
                cell_pos = self.to_2d_index(comb[index])
                next_cell_pos = self.to_2d_index(comb[index + 1])
                next2_cell_pos = self.to_2d_index(comb[index + 2])
                # print('DEBUG')
                # print(cell_pos, next_cell_pos, next2_cell_pos)
                if (board.get(*cell_pos).val != consts.BOARD_DEFAULT_CHAR and
                    board.get(*cell_pos).val == board.get(*next_cell_pos).val
                        and board.get(*cell_pos).val == board.get(*next2_cell_pos).val):
                    return board.get(*cell_pos).val
        return False

    def _min(self, board):
        minEval = 2
        best_move = None
        game_result = self.check_game_end(board)
        if game_result == consts.AI:
            return (1, (0, 0))
        elif game_result == consts.PLAYER:
            return (-1, (0, 0))
        elif not game_result and self.is_draw(board):
            return (0, (0, 0))
        empty_cells = board.get_empty_cells()
        for empty_cell in empty_cells:
            board.place(consts.PLAYER, empty_cell.row, empty_cell.col)
            board.deactivate_cell(empty_cell.row, empty_cell.col)
            m, _ = self._max(board)
            if m < minEval:
                minEval = m
                best_move = empty_cell
            board.place(consts.BOARD_DEFAULT_CHAR,
                        empty_cell.row, empty_cell.col)
            board.activate_cell(empty_cell.row, empty_cell.col)
        return (minEval, best_move)

    def _max(self, board):
        maxEval = -2
        best_move = None
        game_result = self.check_game_end(board)
        if game_result == consts.AI:
            return (1, (0, 0))
        elif game_result == consts.PLAYER:
            return (-1, (0, 0))
        elif not game_result and self.is_draw(board):
            return (0, (0, 0))
        empty_cells = board.get_empty_cells()
        for empty_cell in empty_cells:
            board.place(consts.AI, empty_cell.row, empty_cell.col)
            board.deactivate_cell(empty_cell.row, empty_cell.col)
            m, _ = self._min(board)
            if m > maxEval:
                maxEval = m
                best_move = empty_cell
            board.place(consts.BOARD_DEFAULT_CHAR,
                        empty_cell.row, empty_cell.col)
            board.activate_cell(empty_cell.row, empty_cell.col)
        return (maxEval, best_move)

    def run(self):
        is_game_over = False
        self.board.show()

        while is_game_over == False:
            while True:
                row, col = self.input_pos()
                i_cell = self.board.get(row, col)
                if i_cell.clickable:
                    self.board.place(consts.PLAYER, row, col)
                    self.board.deactivate_cell(row, col)
                    break
                else:
                    print('Already taken! Pick another one!')
            if self.check_game_end(self.board):
                print(f'GAME ENDED AFTER USER!')
                is_game_over = True
                break

            _, ai_pos = self._max(copy.deepcopy(self.board))
            self.board.place(consts.AI, ai_pos.row, ai_pos.col)
            self.board.deactivate_cell(ai_pos.row, ai_pos.col)

            self.board.show()
            if self.check_game_end(self.board):
                print(f'GAME ENDED!')
                is_game_over = True
                break
