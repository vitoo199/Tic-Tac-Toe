import consts


class Human():
    def __init__(self, board):
        self.board = board

    def input(self):
        row = input('Enter row: ')
        col = input('Enter column: ')

        return (int(row) - 1, int(col) - 1)

    def take_position(self, *pos):
        self.board.place(consts.PLAYER, *pos)
