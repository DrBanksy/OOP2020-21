# import unittest

# # from practice_code import Person, Admin, Barber
# from practice_code import A

# class Test(unittest.TestCase):
#     def setUp(self):
#         self.test = A()
    
#     #testing if an error has been raised
#     def test_veryprivate_setter(self):
#         with self.assertRaises(TypeError):
#             self.test.very_private = 0


#     # def setUp(self):
#     #     self.test = Barber('Joe', 12.50, 7)
#     #     self.values =[0, 'Joe']
    
#     # # check that a failure is returned
#     # @unittest.expectedFailure
#     # def test_calculate_salary(self):
#     #     self.assertEqual(self.test.calculate_salary(), self.values[1])
    
#     # # testing if salary is returned
#     # def test_get_salary(self):
#     #     result = self.test.calculate_salary()
#     #     self.assertTrue(result, self.values[0])

# if __name__ == '__main__':
#     unittest.main()