import unittest

from lab3 import WordScramble

class Testing(unittest.TestCase):
    def setUp(self):
        self.test = WordScramble()
        self.values = ['tsetx', 'e']

    @unittest.expectedFailure  
    def test_scramble(self):
        result = self.test.scramble()
        self.assertIn(self.values[1], result)

    

if __name__ == "__main__":
    unittest.main()