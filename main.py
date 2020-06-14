from Board import Board
from Game import Game
from Human import Human
from Computer import Computer

matrix = [
    ['#', '#', '#'],
    ['#', '#', '#'],
    ['#', '#', '#'],
]
b = Board(matrix=matrix)
g = Game(board=b, human=Human(b), computer=Computer(b))
g.run()
