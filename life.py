from collections import defaultdict

class Life():
    def __init__(self, starting_cells=None):
        if starting_cells:
            self.cells = starting_cells
        else:
            self.cells = []

    def next(self, width, height):
        cell_neighbors = defaultdict(int)
        for cell in self.cells:
            self._mark_neighbors(cell, cell_neighbors)

        next_cells = []
        for cell, neighbor_count in cell_neighbors.items():
            if self._is_alive(cell) and neighbor_count == 2:
                next_cells.append(cell)

        board = _make_blank_board(width, height)
        for x, y in next_cells:
            board[x][y] = 1

        return board

    def _mark_neighbors(self, cell, cell_neighbors):
        x, y = cell
        cell_neighbors[(x+1, y+1)]+=1
        cell_neighbors[(x+1, y)]+=1
        cell_neighbors[(x+1, y-1)]+=1
        cell_neighbors[(x, y+1)]+=1
        cell_neighbors[(x, y-1)]+=1
        cell_neighbors[(x-1, y-1)]+=1
        cell_neighbors[(x-1, y)]+=1
        cell_neighbors[(x-1, y-1)]+=1

    def _is_alive(self, cell):
        return cell in self.cells

def _make_blank_board(width, height):
    board = []
    for row in range(height):
        new_row = [0] * width
        board.append(new_row)
    return board
