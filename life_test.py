import unittest

class TestLife(unittest.TestCase):

    def test_next__returns_blank_board_of_requested_dimensions_if_no_starting_items(self):
        width = 20
        height = 10
        life = Life()

        next_board = life.next(width, height)
        expected_board = [[0]*width]*height

        self.assertEqual(next_board, expected_board, 'Next() did not return a blank board.')



if __name__ == '__main__':
    unittest.main()
