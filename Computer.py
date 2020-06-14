import consts
import copy


class Computer():
    def __init__(self, board):
        self.board = board
        self.game = None

    def set_game(self, game):
        self.game = game

    def find_best_move(self):
        if self.game:
            return self._max(self.board)

    def _min(self, board):
        minEval = 2
        best_move = None
        game_result = self.game.check_game_end(board)
        if game_result == consts.AI:
            return (1, (0, 0))
        elif game_result == consts.PLAYER:
            return (-1, (0, 0))
        elif not game_result and self.game.is_draw(board):
            return (0, (0, 0))
        empty_cells = board.get_empty_cells()
        for empty_cell in empty_cells:
            board.place(consts.PLAYER, empty_cell.row, empty_cell.col)
            board.deactivate_cell(empty_cell.row, empty_cell.col)
            (m, _) = self._max(board)
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
        # print('-----------------')
        # board.show()
        # print('-----------------')
        game_result = self.game.check_game_end(board)
        if game_result == consts.AI:
            return (1, (0, 0))
        elif game_result == consts.PLAYER:
            return (-1, (0, 0))
        elif not game_result and self.game.is_draw(board):
            return (0, (0, 0))
        empty_cells = board.get_empty_cells()
        for empty_cell in empty_cells:
            board.place(consts.AI, empty_cell.row, empty_cell.col)
            board.deactivate_cell(empty_cell.row, empty_cell.col)
            (m, _) = self._min(board)
            if m > maxEval:
                maxEval = m
                best_move = empty_cell
            board.place(consts.BOARD_DEFAULT_CHAR,
                        empty_cell.row, empty_cell.col)
            board.activate_cell(empty_cell.row, empty_cell.col)
        return (maxEval, best_move)

    def take_position(self, *pos):
        self.board.place(consts.AI, *pos)
