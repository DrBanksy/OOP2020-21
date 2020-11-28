'''
Demonstrating composition
'''


# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus 
    
#     def annual_salary(self):
#         return(self.pay*12) + self.bonus

# class Employee:
#     def __init__(self,name, age, pay,bonus):
#         self.name = name
#         self.age = age
#         # delegating some responsibility from a Salary class to an employee class
          # part of i.e. salary is part of employee
          #not indepndent
#         self.obj_salary= Salary(pay,bonus)

#     def total_salary(self):
#         return self.obj_salary.annual_salary()
    

# emp1 = Employee("John", 23, 23.80, 100)
# print(emp1.total_salary())



'''
Demonstrating aggregation 
'''



# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus  
    
#     def annual_salary(self):
#         return(self.pay*12) + self.bonus

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         # HAS A relationship
#         self.obj_salary=salary

#     def total_salary(self):
#         return self.obj_salary.annual_salary()

# # unidirectional, just passing salary object to the employee class, not the other way round
# # both of these obects exist independent of one another
# salary = Salary(23.80, 100)
# emp1 = Employee("John", 23, salary)
# print(emp1.total_salary())



'''
Demonstrating Non local keyword
'''

# def outerfunction():
#     num1 = 5

#     def innerfunction():
#         nonlocal num1
#         num1 = 10
#         second_num=1
#         print(f'inner - second_num is: {second_num}')
    
#     innerfunction()
#     print(f'outer - first num is: {num1}')

# outerfunction()


'''
super()
'''

class Parent:
    def __init__(self, name):
        print('Parent __init__', name)
    
class Child(Parent):
    def __init__(self):
        print('Child __init__')
        super().__init__("Cormac")

person1 = Child()
print(Child.__mro__)
