class Cell():
    def __init__(self, row, col, val='', clickable=False):
        self.row = row
        self.col = col
        self.val = val
        self.clickable = clickable

    def deactivate(self):
        self.clickable = False

    def activate(self):
        self.clickable = True
