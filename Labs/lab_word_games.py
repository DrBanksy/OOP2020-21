# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:

    def __init__(self):
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        return self.__my_words

    def word_play(self):
        print("User input was: "+self.the_words)

class WordDuplication(WordGames): # you implement this and provide docstrings
    def word_play(self):
        print("User input doubled: ")
        print(self.the_words + ' ' + self.the_words)


class WordScramble(WordGames): # you implement this and provide docstrings
    def word_play(self):
        users_sentence = list(self.the_words.split())   
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


# wg = WordGames()
# wg.word_play()
# wd = WordDuplication()
# wd.word_play()
scramble = WordScramble()
scramble.word_play()
