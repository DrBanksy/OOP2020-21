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
        print("first character: " + message[0])
        print("last character: " + message[-1])

        # use slice notation:
        print("print from position 3 to end: " + message[3:0])
        print("print up to position 3: " + message[:3])


        # escaping a character:
        message2 = "O\'Brien"
        print(message2)

        # find all a's in the input word aaand count how many there are:
        lower_message = message.lower()
        print("all lower characters: " + lower_message)
        print("the first ocurence of a is at position: ", lower_message.find('a'))
        print("there are "+ str(lower_message.count('a')) + "a's in the word.")
        print("total character count is: " +str(len(lower_message)))


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        # message[0] = '-'as
        print(message.replace('a', '-'))
        


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        user_list = (list(message.split(" ")))
        print(user_list)

        # append a new element to the list and print:
        user_list.append("new")
        print(user_list)

        # remove from the list in 3 ways:
        # user_list.pop()
        # user_list.remove("cake")
        del user_list[-1]
        print(user_list)
        

        # check if the word cake is in your input list:
        print('cake' in user_list)

        # reverse the items in the list and print:
        # user_list.reverse()
        # print(user_list)

        # # reverse the list with the slicing trick:
        # print(user_list[::-1])
        # print(user_list)

        # # print the list 3 times by using multiplication:
        # print(user_list*3)



tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()
