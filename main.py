from Board import Board
from Game import Game


matrix = [
    ['#', '#', '#'],
    ['#', '#', '#'],
    ['#', '#', '#'],
]

# t_matrix = [
# ['#', '#', 'O'],
# ['#', 'X', 'O'],
# ['X', 'X', 'O'],
# ]
b = Board(matrix=matrix)
g = Game(board=b)
g.run()

# test = Board(t_matrix)
# print(g.check_game_end(test))
