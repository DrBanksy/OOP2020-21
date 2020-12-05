# OOP Python Lab on Pyton Testing
# File provided via github.
# lab for testing
# you should recognise some of this code from a
# previous lab
# author: B. Schoen-Phelan
# date: 04-12-2020

class TypesAndStrings:

    def last_char(self, value):
        print("Originally entered: ", value)
        if not isinstance(value, str):
            raise TypeError("Wrong type, we need a string")

        # return the last character
        return value[-1]

    def first_char(self, value):
        print("Originally entered: ", value)
        if not isinstance(value, str):
            raise TypeError("Wrong type, we need a string")

        return value[0]

    def replace_all_a(self, value):
        print("Originally entered: ", value)
        if not isinstance(value, str):
            raise TypeError("Wrong type, please enter a string")
        return value.replace('a','-')


    def all_lower(self, value):
        return value # issue here, should show up in testing
    


# test = TypesAndStrings()
# print(test.replace_all_a('tatatta'))