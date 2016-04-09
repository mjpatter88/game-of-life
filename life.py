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
            if self._is_alive(cell) and neighbor_count in (2, 3):
                next_cells.append(cell)
            if not self._is_alive(cell) and neighbor_count == 3:
                next_cells.append(cell)

        self.cells = next_cells

        return self._get_current_board(width, height)

    def _get_current_board(self, width, height):
        board = _make_blank_board(width, height)
        for row, col in self.cells:
            board[row][col] = 1
        return board

    def _mark_neighbors(self, cell, cell_neighbors):
        row, col = cell
        cell_neighbors[(row+1, col+1)]+=1
        cell_neighbors[(row+1, col)]+=1
        cell_neighbors[(row+1, col-1)]+=1
        cell_neighbors[(row, col+1)]+=1
        cell_neighbors[(row, col-1)]+=1
        cell_neighbors[(row-1, col-1)]+=1
        cell_neighbors[(row-1, col)]+=1
        cell_neighbors[(row-1, col+1)]+=1

    def _is_alive(self, cell):
        return cell in self.cells

def _make_blank_board(width, height):
    board = []
    for row in range(height):
        new_row = [0] * width
        board.append(new_row)
    return board
