import unittest

from tic_tac_toe import we_have_winner



#FIXME Что тут тестить?

class Test(unittest.TestCase):
    
    def test_winner(self):
        self.assertEqual(we_have_winner(['X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O']), 'noone')

    

if __name__ == '__main__':
    unittest.main()