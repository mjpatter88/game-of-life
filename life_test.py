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

    def test_next__called_twice_block_of_four_living_all_stay_alive(self):
        starting_cells = [(1,1), (1,2), (2,1), (2,2)]
        life = Life(starting_cells)

        next_board =life.next(self.width, self.height)
        next_board = life.next(self.width, self.height)

        self.assertEqual(next_board[1][1], 1, 'Board[1][1] was not alive.')
        self.assertEqual(next_board[1][2], 1, 'Board[1][2] was not alive.')
        self.assertEqual(next_board[2][1], 1, 'Board[2][1] was not alive.')
        self.assertEqual(next_board[2][2], 1, 'Board[2][2] was not alive.')

    def test_next__doesnt_break_on_negative_column_numbers(self):
        starting_cells = [(0,0), (1,0), (2,0)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)
        expected_board = [
                [0,0,0,0,0],
                [1,1,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'negative numbers not handled correctly.')

        next_board = life.next(self.width, self.height)
        expected_board = [
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'negative numbers not handled correctly.')

    def test_next__doesnt_break_on_negative_row_numbers(self):
        starting_cells = [(0,0), (0,1), (0,2)]
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)
        expected_board = [
                [0,1,0,0,0],
                [0,1,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'negative numbers not handled correctly.')

        next_board = life.next(self.width, self.height)
        expected_board = [
                [1,1,1,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'negative numbers not handled correctly.')

    def test_next__preserves_the_beacon_oscillation(self):
        height = 6
        width = 6
        starting_cells = [(1,1), (1,2), (2,1), (2,2), (3,3), (3,4), (4,3), (4,4)]
        life = Life(starting_cells)

        next_board = life.next(width, height)
        expected_board = [
                [0,0,0,0,0,0],
                [0,1,1,0,0,0],
                [0,1,0,0,0,0],
                [0,0,0,0,1,0],
                [0,0,0,1,1,0],
                [0,0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'Beacon oscillation phase 1 not generated.')

        next_board = life.next(width, height)
        expected_board = [
                [0,0,0,0,0,0],
                [0,1,1,0,0,0],
                [0,1,1,0,0,0],
                [0,0,0,1,1,0],
                [0,0,0,1,1,0],
                [0,0,0,0,0,0]]
        self.assertEqual(next_board, expected_board, 'Beacon oscillation phase 2 not generated.')

if __name__ == '__main__':
    unittest.main()
