import unittest

from week11 import TypesAndStrings

class FirstTest(unittest.TestCase):
    def setUp(self):
        self.test = TypesAndStrings()
    
    @unittest.expectedFailure
    def test_last_char(self):
        # self.assertRaises(TypeError, self.test.first_char, 5)
        self.assertEqual(self.test.last_char('test'), 5)
    
    @unittest.expectedFailure
    def test_first_char(self):
        self.assertRaises(TypeError, self.test.first_char, 'hello')
    
    def test_replace_all_a(self):
        self.assertEqual(self.test.replace_all_a('tata'), 't-t-')


if __name__ == "__main__":
    unittest.main()