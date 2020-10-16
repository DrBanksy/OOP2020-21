# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3
import string
import scapy


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        

    def scramble(self):
        users_sentence = list(self.user_input.split())
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        for word in users_sentence:
            if (len(word) <= 3):
                print(word, end=" ")
            else:
                complete_word = word
                new_word = word[1:-1]
                
                letters = list(new_word.lower())
                i = 0
                while i < len(letters)-1:
                        if i == len(letters)-1:
                            break

                        if letters[-1] == '.' or ',':
                            if i < len(letters)-2:
                                temp = letters[i]
                                letters[i] = letters[i+1]
                                letters[i+1] = temp
                                i+=1
                            else:
                                break
                        else:
                            temp = letters[i]
                            letters[i] = letters[i+1]
                            letters[i+1] = temp
                            i+=1
                starting_letter = complete_word[0]
                ending_letter = complete_word[-1]
                letters = [''.join(letters)]
                new_word = starting_letter + letters[0] + ending_letter
                print(new_word, end = " ")
                
                


                    
                
                
                # position1 = self.user_input[1]
                # position2 = self.user_input[2]
                # users_word = self.user_input[0] + ''.join(position2) + ''.join(position1) + self.user_input[3:]
                # print (users_word)


            

            
            


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

