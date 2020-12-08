from lab_word_games import WordDuplication, WordScramble

class NewGame(WordScramble, WordDuplication):
    pass


game = NewGame()
print(NewGame.__mro__)