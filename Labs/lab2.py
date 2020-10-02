#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        testt = message[-1]
        print(testt)

        # use slice notation:
        message1 = message[0:2]
        print(message1)

        # escaping a character:
        message2 = "O\'Brien"
        print(message2)

        # find all a's in the input word aaand count how many there are:
        print(message.find('a'))
        print(message.count('a',0,-1))


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        # message[0] = '-'
        message3 = message.replace('a', '-')
        print(message3)
        


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        user_list = (list(message.split(" ")))
        print(user_list)

        # append a new element to the list and print:
        user_list.append("b")
        user_list.append("c")
        user_list.append("d")
        user_list.append("e")
        # user_list.append("cake")
        print(user_list)

        # remove from the list in 3 ways:
        # del user_list[0]
        # del user_list[0:4]
        # user_list.remove('a')  --> removes first ocurrence only 
        # del user_list[2:]
        # print(user_list)

        # check if the word cake is in your input list:
        if 'cake' in user_list:
            print("cake is in the list")

        # reverse the items in the list and print:
        user_list.reverse()
        print(user_list)

        # reverse the list with the slicing trick:
        print(user_list[::-1])
        print(user_list)

        # print the list 3 times by using multiplication:
        print(user_list*3)



tas = Types_and_Strings()
tas.play_with_strings()
# tas.play_with_lists()
