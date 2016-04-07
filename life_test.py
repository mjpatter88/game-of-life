import unittest

from life import Life

class TestLife(unittest.TestCase):
    def setUp(self):
        self.width = 20
        self.height = 10

    def test_next__returns_blank_board_of_requested_dimensions_if_no_starting_items(self):
        life = Life()

        next_board = life.next(self.width, self.height)
        expected_board = [[0]*self.width]*self.height

        self.assertEqual(next_board, expected_board, 'Next() did not return a blank board.')

    def test_next__returns_blank_board_if_all_starting_cells_dead(self):
        starting_cells = []
        life = Life(starting_cells)

        next_board = life.next(self.width, self.height)
        expected_board = [[0]*self.width]*self.height

        self.assertEqual(next_board, expected_board, 'Next() did not return a blank board.')


if __name__ == '__main__':
    unittest.main()
