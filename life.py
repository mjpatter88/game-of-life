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
        for row in range(height):
            for col in range(width):
                if (row, col) in self.cells:
                    board[row][col] = 1
        return board

    def _mark_neighbors(self, cell, cell_neighbors):
        row, col = cell
        cell_neighbors[(row-1, col-1)]+=1
        cell_neighbors[(row-1, col)]+=1
        cell_neighbors[(row-1, col+1)]+=1
        cell_neighbors[(row, col+1)]+=1
        cell_neighbors[(row, col-1)]+=1
        cell_neighbors[(row+1, col-1)]+=1
        cell_neighbors[(row+1, col)]+=1
        cell_neighbors[(row+1, col+1)]+=1

    def _is_alive(self, cell):
        return cell in self.cells

def _make_blank_board(width, height):
    return [[0]*width for row in range(height)]


if __name__ == '__main__':
    import os
    import sys
    import time
    import pprint
    from ast import literal_eval

    filename = sys.argv[1] if len(sys.argv) >= 2 else 'beacon.txt'
    width = int(sys.argv[2]) if len(sys.argv) >= 3 else 6
    height = int(sys.argv[3]) if len(sys.argv) >= 4 else 6
    speed = int(sys.argv[4]) if len(sys.argv) >= 5 else 4

    starting_cells = []
    with open(filename, 'r') as in_file:
        for line in in_file.readlines():
            if line[0] == '(':
                starting_cells.append(literal_eval(line))

    life = Life(starting_cells)

    circle = '\u25CF'
    rectangle = '\u25A0'

    for x in range(1000):
        os.system('clear')
        board = life.next(width, height)
        for row in board:
            for col in row:
                if col:
                    print(rectangle, end='')
                else:
                    print(' ', end='')
            print()
        print("\n\nIteration: {}".format(x))
        time.sleep(1.0/speed)
