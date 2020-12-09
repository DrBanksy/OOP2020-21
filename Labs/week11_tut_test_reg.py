import unittest

# from week11_tut import MyDemo

# class Testing(unittest.TestCase):
#     def setUp(self):
#         self.nums = MyDemo([1,2,3,4,5,6,7,7,7])
    
#     def test_mean(self):
#         self.assertEqual(self.nums.mean(), 4.666666666666667)
    

# if __name__ == '__main__':
#     unittest.main()

from lab_registration_record import RegistrationData, Student

class Testing(unittest.TestCase):
    def setUp(self):
        self.test = RegistrationData("123 fake street", 0, "undergraduate", "Tom", "Smith", "c19313793")
        self.list = ['Tom', 'barry', 'mark']
    
    @unittest.expectedFailure
    def test_address_property(self):
        self.assertNotIn(self.test.student_object_property.student_name[0], self.list)

if __name__ == '__main__':
    unittest.main()