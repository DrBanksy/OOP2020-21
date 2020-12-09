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


#INHERITANCE


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


#INHERITANCE

# class A:

#     pass


# class B(A):

#     pass 

# a = A()

# b = B()

# print(type(b)==B)
# print(isinstance(b,A))


#ABSTRACT CLASSES


# from abc import ABC, abstractmethod

# class Polygon(ABC):

#     @abstractmethod
#     def no_of_sides(self):
#         pass

#     def what_am_i(self):
#         print("I am a parent polygon")
    
#     @property
#     @abstractmethod
#     def length(self):
#         pass


# class Triangle(Polygon):
#     def __init__(self):
#         self.__x = 0

#     def no_of_sides(self):
#         print('I have three sides')

#     def what_am_i(self):
#         print('I am a child triangle')
#         super().what_am_i()
    
#     @property
#     def length(self):
#         return self.__x
    
#     @length.setter
#     def length(self, value):
#         self.__x = value


# t= Triangle()
# t.what_am_i()
# t.length = 5
# print(t.length)



#POLYMORPHISM

# class Cat:
#     def makeSound(self):
#         print('meow')
    
# class Dog:
#     def makeSound(self):
#         print('wouff')

# def speak(animal):
#     animal.makeSound()

# cat = Cat()
# dog = Dog()

# speak(cat)


#COMPOSITION

# class Salary:

#    def __init__(self, pay, bonus):
#        self.__pay = pay
#        self.__bonus = bonus

#    def __str__(self):
#        return f"I earn {self.pay_prop} and my bonus is: {self.bonus_prop}"

#    @property
#    def pay_prop(self):
#        return self.__pay

#    @pay_prop.setter
#    def pay_prop(self, value):
#        self.__pay = value

#    @property
#    def bonus_prop(self):
#        return self.__bonus

#    @bonus_prop.setter
#    def bonus_prop(self, value):
#        self.__bonus = value

#    # returns a calculation
#    def annual_salary(self):
#        return (self.pay_prop * 12) + self.bonus_prop


# # composition:

# class Employee:
#    def __init__(self, name, age, pay, bonus):
#        self.__name = name
#        self.__age = age
#        self.__salary_object = Salary(pay, bonus)

#    @property
#    def age_prop(self):
#        return self.__age

#    @age_prop.setter
#    def age_prop(self, value):
#        self.__age = value

#    @property
#    def name_prop(self):
#        return self.__name

#    # if you don't provide a setter property, then this
#    # variable cannot be set!

#    @property
#    def salary_prop(self):
#        return self.__salary_object

#    def total_salary(self):
#        return self.salary_prop.annual_salary()


# anna = Employee("Anna", 25, 2500, 10000)
# print(anna.total_salary())
# print(anna.salary_prop)  



# STATIC AND CLASSMETHODS

# class DifferentMethodsClass:
#    class_attribute = "This is a class attribute"

#    def __init__(self):
#        self.instance_attributes = "This is an instance attribute"

#    def instance_method(self):  # usual argument self
#        print('instance method called', self)

#    @classmethod
#    def class_method(cls):
#        print('class method called', cls)
#        # print(self.instance_attributes)  # this will 
#   # fail
#        print("class attribute: ", cls.class_attribute)

#    @staticmethod
#    def static_method():
#        print('static method called')



# demo = DifferentMethodsClass()
# demo.instance_method()
# demo.class_method()  
# demo.static_method()

# DifferentMethodsClass.class_method()  
# DifferentMethodsClass.static_method()  
# # DifferentMethodsClass.instance_method()  # error


# class A:
#     CLASS_ATTRIBUTE = ["a", "b", "c"]

#     def __init__(self):
#         self.instance_atrribute = ["x", "y"]
    
#     def instance_method(self):
#         print('This is an instance method')
    
#     @classmethod
#     def class_method(cls):
#         print('this is a class method')
    
#     @staticmethod
#     def static_method():
#         print('static method')
    
# demo1 = A()
# demo2 = A()

# print(demo1.CLASS_ATTRIBUTE)
# demo2.CLASS_ATTRIBUTE.append('x')
# print(demo1.CLASS_ATTRIBUTE)

# print(demo1.instance_atrribute)
# demo1.instance_atrribute.append('a')
# print(demo1.instance_atrribute)



# static and class methods

# class Student:
#     COURSES = ['Maths', 'Programming']

#     def __init__(self):
#         self.instance_attribute = 5
    
#     @classmethod
#     def class_method(cls):
#         # accessing class attributes fine
#         for course in cls.COURSES:
#             print(course)
        
#         # trying to access instance attribute DOESNT WORK
#         # print(f"{cls.instance_attribute}")

#     @staticmethod
#     def calculate_student_fee(num1):
#         pass



# stu1 = Student()
# stu1.class_method()
    

    