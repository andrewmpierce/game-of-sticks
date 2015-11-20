import unittest
from sticks import *

class TestSticks(unittest.TestCase):

    def test_is_game_over(self):
        self.assertTrue(is_game_over(0))
        self.assertTrue(is_game_over(-1))
        self.assertFalse(is_game_over(3))
        self.assertTrue(is_game_over(-1))

    def test_who_lost(self):
        self.assertEqual(who_lost("Bill", 1), "Bill")
        self.assertEqual(who_lost("Bill", 0), "Bill")
    
if __name__ == '__main__':
    unittest.main()
