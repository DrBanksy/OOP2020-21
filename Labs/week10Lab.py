from abc import ABC, abstractmethod
import sys
from numpy import random

#author: Cormac Smith
#date: 28/11/2020

# TODO
# look at static methods
# implement try...except

class MathsGame(ABC):
    '''
    this abstract class defines a foundation for each maths game

    Methods:
        __init__ : abstract method
            prints a welcome message

        user_input: abstract property    
            pass
    
        play_game : abstract method

    '''
    @abstractmethod
    def __init__(self):
        print("Welcome to the maths game")
    
    @abstractmethod
    def play_game(self):
        pass
    
    @property
    @abstractmethod
    def user_input(self):
        pass


class Fibonacci(MathsGame):
    '''
    This class inherits methods/properties from the abstract class
    MathsGame. 

    Attributes:
        __correct_guesses -> keeps tracks of users correct guesses
        __choice -> stores users choice: either 1 or 2
    
    Methods:
        __init__ : 
        calls parent init
        sets correct guesses to 0

        user_input : property
        returns users input

        correct_guesses : property
        returns correct guesses made by user

        play_game(self):
        handles the gameplay logic
        makes call to a static method to calc next num

        calculate_next(first_num, second_num) : static method
        Takes two numbers and returns the next number in the 
        fibonacci sequence


    '''
    def __init__(self):
        super().__init__()
        self.__correct_guesses = 0
        self.play_game()

    @property
    def user_input(self):
        return self.__choice

    @property
    def correct_guesses(self):
        return self.__correct_guesses 
     

    def play_game(self):
        while(1):
            self.fibonacci_nums = []
            try:
                self.__choice = int(input("Enter 1 to play, Enter 2 to exit: "))
                if(self.__choice > 2 or self.__choice < 1 ):
                    print("Must enter 1 or 2")
                    self.play_game()
            except ValueError:
                print("Input an integer")
                self.play_game()
     
            if(self.__choice == 2 ):
                print('Correct guesses: ', self.correct_guesses)
                print("exiting...")
                start.display_menu()

            terms  = int(input("How many terms: "))
            count = 0
            first_num = 0
            second_num = 1

            if(terms <= 0):
                print("Must be greater than 0")
                self.play_game()
            elif(terms == 1):
                print(first_num)
            else:
                while(count < terms):
                    next_num = self.calculate_next(first_num, second_num)
                    first_num = second_num
                    second_num = next_num
                    self.fibonacci_nums.append(first_num)
                    if(count == terms - 2):
                        print(self.fibonacci_nums)
                        user_guess = int(input("Guess next num: "))
                        if (user_guess != next_num):
                            print("Sorry this is wrong")
                            print(f" The right number is {next_num}")
                        else:
                            self.__correct_guesses += 1
                            print("Well done")
                    count += 1
         

    @staticmethod
    def calculate_next(first_num, second_num):
        ans = first_num + second_num
        return ans

        
class GuessTheNum(MathsGame):
    '''
    This class inherits from MathsGame. User has two attempts at guessing a random
    number between 0-10 inclusive

    attributes:
        __limit 
        sets the amount of attempts we give the user

    method:
        __init__:
        makes call to super

        generate_random_num : static methods
        returns a random integer

        random_num : property
        returns the random number stored in __random

        user_input : property
        returns users input

        play_game :
        handles gameplay logic
        makes call to static method generate_random_num

    '''
    def __init__(self):
        super().__init__()
        self.play_game()
    
    @staticmethod
    def generate_random_num():
       return random.randint(10)

    @property
    def user_input(self):
        pass

    @property
    def random_num(self):
        return self.__random_num
    
    def play_game(self):
        self.__limit = 2
        self.__random_num = self.generate_random_num()

        while(self.__limit != 0):
            try:
                user_guess = int(input("Guess a number between 0-10: "))
            except ValueError:
                print("Not a valid guess")
                self.play_game()
            if(user_guess != self.random_num):
                print("wrong!!")
                self.__limit = self.__limit - 1
            else:
                print("Congrats you guessed correctly !!!")
                print("Play again: Y/N")
                choice = input("")
            
                if(choice == 'Y' or choice == 'y'):
                    self.play_game()

                elif(choice == 'N' or choice == 'n'):
                    start.display_menu()                
        
        if(self.__limit == 0):
            print("Your out of guesses")
            print("Play again: Y/N")
            choice = input("")

            if(choice == 'Y' or choice == 'y'):
                self.play_game()

            elif(choice == 'N' or choice == 'n'):
                start.display_menu()
            
class Menu:
    '''
    Class which provides a menu for the maths games. if option 1 is picked
    we create a Fibonacci object. If 2 is picked we create GuessTheNum object

    Attributes:
        choice:
            stored the users choice
        
        methods:
            display_menu(self):
                presents the user with options and creates and runs game
                specfied by the user
            
    '''
    def display_menu(self):
        print("Pick a game")
        print("1) Fibonacci ")
        print("2) Guessing game")
        try:
            choice = int(input("Choose your game: "))
        except ValueError:
            print("Not a valid option")
            start.display_menu()

        if(choice == 2):
            game2 = GuessTheNum()
        elif(choice == 1):
            game1 = Fibonacci()
        

start = Menu()
start.display_menu()
# play = Fibonacci()