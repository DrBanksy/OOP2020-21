# class MyDog:
#     def __init__(self, name, age=0):
#         self.__name = name
#         self.__age = age

#     @property
#     def print_name(self):
#         return self.__name
        
#     @property
#     def print_age(self):
#         return self.__age


# obj1 = MyDog('Lucky')
# print(obj1.print_name)
# print(obj1.print_age)

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
    
#     @property
#     def get_name(self):
#         return self.__name

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         self.student_id = student_id
#         self.__age = age
#         super().__init__(name, age)
    
#     def enroll_into_uni(self):
#         print("Enrolled")

#     @property
#     def get_age(self):
#         return self.__age

# stu1 = Student('Cormac', 20, 'c19313793')
# print(stu1.get_age)

# class A:
#   def __init__(self):
#     print("I'm class A")

# class B(A):
#   pass

# a = A()
# b = B()

# # usage of isinstance
# print(isinstance(21, int))
# print(isinstance(a,A))
# print(isinstance(b,A))

# print(type(21))
# print(type(a))
# print(type(b))
# print(type(b)==A, type(b)==B)

# class Person:
#   def __init__(self, f_name, l_name):
#     self.first_name = f_name
#     self.last_name = l_name

#   def print_name(self):
#     print(self.first_name, self.last_name)

# class Student(Person):
#   def __init__(self, s_id, f_name, l_name):
#       super().__init__(f_name, l_name)
#       self.student_id = s_id

# stu1 = Student('c19313793','Cormac', 'Smith')
# stu1.print_name()

# class A:
#   def __init__(self):
#     self.public = "Lecturer"
#     self._private = "Bianca"
#     self.__very_private = "Phelan"

#   @property
#   def very_private(self):
#     return self.__very_private

#   @very_private.setter
#   def very_private(self, value):
#     if type(value) == str:
#       self.__very_private = value
#     else:
#       raise TypeError("Error, cannot set this value.")

# p = A()
# try:
#     p.very_private = 1
# except TypeError as e:
#     print("Could not set second name")


# class Person:
#  def __init__(self, f_name, l_name):
#    self.__first_name = f_name
#    self.__last_name = l_name

#  @property
#  def first_name(self):
#    # include validation if needed, maybe we return names
#    # only on a Wednesday, or some business logic like that
#    return self.__first_name

#  @property
#  def last_name(self):
#    return self.__last_name

#  @last_name.setter
#  def last_name(self, value):
#    # imagine some validation here
#    self.__last_name = value

#  def print_name(self):
#    print(self.first_name, self.last_name)


# class Student(Person):
#   def __init__(self, s_id, f_name, l_name):
#     super().__init__(f_name, l_name)
#     self.__student_id = s_id

#   @property
#   def get_student_id(self):
#     return self.__student_id

#   def get_full_details(self):
#     return super().first_name, super().last_name, self.get_student_id
 
# bryan = Student(1234, "Bryan", "Duggan")
# print(bryan.get_full_details())
# bryan.last_name = "smith"
# print(bryan.get_full_details())

# class A:

#     pass


# class B(A):

#     pass 

# a = A()

# b = B()

# print(type(b)==B)

# print(isinstance(b,A))

