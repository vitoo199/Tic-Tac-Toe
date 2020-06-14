from Cell import Cell
import consts


class Board():
    def __init__(self, matrix):
        self.cells = self._create_cells(matrix)

    def _create_cells(self, matrix):
        arr = []
        for row_index in range(len(matrix)):
            row = []
            for char_index in range(len(matrix[row_index])):
                row.append(
                    Cell(row=row_index, col=char_index,
                         val=matrix[row_index][char_index], clickable=True)
                )
            arr.append(row)
        return arr

    def place(self, mark, *pos):
        self.get(*pos).val = mark

    def get_empty_cells(self):
        return [cell for cell_row in self.cells for cell in cell_row if cell.clickable or cell.val == consts.BOARD_DEFAULT_CHAR]

    def show(self):
        for i in range(consts.ROW):
            tmp = ''
            for j in range(consts.COLUMN):
                tmp += self.get(i, j).val
            print(' '.join(tmp))
            tmp = ''

    def get(self, *pos):
        return self.cells[pos[0]][pos[1]]

    def deactivate_cell(self, *pos):
        self.get(*pos).deactivate()

    def activate_cell(self, *pos):
        self.get(*pos).activate()
