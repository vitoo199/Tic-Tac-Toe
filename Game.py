from Cell import Cell
import consts


class Game():
    def __init__(self, board, human, computer):
        self.board = board
        self.human = human
        self.computer = computer
        self.computer.set_game(self)
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
        return len(board.get_empty_cells()) == 0 and not self.check_game_end(board)

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

                if (board.get(*cell_pos).val != consts.BOARD_DEFAULT_CHAR and
                    board.get(*cell_pos).val == board.get(*next_cell_pos).val
                        and board.get(*cell_pos).val == board.get(*next2_cell_pos).val):
                    return board.get(*cell_pos).val
        return False

    def is_valid_move(self, move):
        row, col = move
        if row >= consts.ROW or row < 0:
            return False
        if col >= consts.COLUMN or col < 0:
            return False
        if not self.board.get(*move).clickable:
            return False
        return True

    def run(self):
        is_game_over = False
        self.board.show()
        while not is_game_over:
            while True:
                human_pos = self.human.input()
                if self.is_valid_move(human_pos):
                    self.human.take_position(*human_pos)
                    self.board.deactivate_cell(*human_pos)
                    break
                else:
                    print('Bad position or already taken! Pick another one!')
            if self.check_game_end(self.board):
                print(f'GAME HAS ENDED!')
                is_game_over = True
                break

            _, ai_pos = self.computer.find_best_move()
            self.computer.take_position(*(ai_pos.row, ai_pos.col))
            self.board.deactivate_cell(*(ai_pos.row, ai_pos.col))

            self.board.show()
            if self.check_game_end(self.board):
                print(f'GAME HAS ENDED!')
                is_game_over = True
                break
