import unittest

from life import Life

class TestLife(unittest.TestCase):
    def setUp(self):
        self.width = 5
        self.height = 4
        self.expected_board = []
        for row in range(self.height):
            new_row = [0] * self.width
            self.expected_board.append(new_row)

    def test_next__returns_blank_board_of_requested_dimensions_if_no_starting_items(self):
        life = Life()

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board, self.expected_board, 'Next() did not return a blank board.')

    def test_next__returns_blank_board_if_all_starting_cells_dead(self):
        starting_cells = []
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board, self.expected_board, 'Next() did not return a blank board.')

    def test_next__one_live_cell_with_two_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[1][2], 1, 'Board[1][2] was not alive.')

    def test_next__one_live_cell_with_three_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3), (2,2)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[1][2], 1, 'Board[1][2] was not alive.')

    def test_next__one_live_cell_with_one_live_neighbors_dies(self):
        starting_cells = [(1,1), (1,2)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[1][2], 0, 'Board[1][2] was not dead.')

    def test_next__one_live_cell_with_zero_live_neighbors_dies(self):
        starting_cells = [(1,1)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[1][1], 0, 'Board[1][1] was not dead.')

    def test_next__one_dead_cell_with_three_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[2][2], 1, 'Board[2][2] was not alive.')

if __name__ == '__main__':
    unittest.main()
