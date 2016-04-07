import unittest

class TestLife(unittest.TestCase):

    def test_first_test(self):
        self.assertEqual(1, 2, 'Failing test')



if __name__ == '__main__':
    unittest.main()
