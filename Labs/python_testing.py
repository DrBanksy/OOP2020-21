import unittest

from week11 import TypesAndStrings

class FirstTest(unittest.TestCase):
    def setUp(self):
        self.test = TypesAndStrings()
        self.value = ["HALLO", 123]

    def test_last(self):
        result = self.test.last_char(self.value[0])
        self.assertEqual(result, self.value[0][-1])

    @unittest.expectedFailure
    def test_last_expect_failure(self):
        result = self.test.last_char(self.value[0])
        self.assertEqual(result, self.value[0][0])
    
    def test_replacing_a(self):
        result = self.test.replace_all_a(self.value[0].lower())
        print("+++++ ", result)
        self.assertNotIn(result, 'a')

    
    def test_assertion_no_str(self):
        with self.assertRaises(TypeError):
            self.test.first_char(self.value[1])
    
    def test_first_char(self):
        result = self.test.first_char(self.value[0])
        self.assertTrue(result, self.value[0][0])

    def test_lower(self):
        result = self.test.all_lower(self.value[0])
        self.assertEqual(result, self.value[0].lower())


if __name__ == "__main__":
    unittest.main()