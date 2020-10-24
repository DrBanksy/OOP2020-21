# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        card_name = self.the_cards.get()
        the_card = PhotoImage(file=f'Labs\\cards\\{card_name}')
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        
        self.closed_deck = Button(cards_frame, state='normal')
        closed_card = PhotoImage(file='Labs\\cards\\closed_deck.gif')
        self.closed_deck.config(image=closed_card)
        self.closed_deck.grid(row=0, column=1, padx=2, pady=2)
        self.closed_deck.photo = closed_card
        self.closed_deck['command'] = self.pick_card
        
        
        self.done_button = Button(button_frame, text="I'm done!", command=self.done_playing, state='normal')
        self.done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()
        self.update_score(card_name)
        
        

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        cards = Queue(maxsize=52) #change this if you want to use a different data structure
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        card_list = []

        # your code goes here:
        for suit in suits:
            for v in range(1,11):
                card_list.append(f"{v}_{suit}.gif")
            for p in people:
                card_list.append(f"{p}_{suit}.gif")           
        shuffle(card_list)
        

        # your code goes here:
        for card in card_list:
            cards.put(card)

        return cards

    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        
        new_card = self.the_cards.get()
        new_image = PhotoImage(file=f'Labs\\cards\\{new_card}')
        self.open_card.config(image=new_image)
        self.open_card.photo = new_image
        self.update_score(new_card)

        self.open_card.update_idletasks()

        self.check_scores()

        

        

        
        

        

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):
        print("test")
        score = self.player_score
        if(score > 21 ):
            self.score_label.config(text="Your score: " + str(self.player_score) + " Bad luck, Game OVER!" )
            self.score_label.update_idletasks()
            self.closed_deck.config(state=DISABLED)
            self.done_button.config(state=DISABLED)
        elif(score == 21):
            self.score_label.config(text="Your score: " + str(self.player_score) + ". You hit the jack pot!" )
            self.score_label.update_idletasks()
            self.closed_deck.config(state=DISABLED)
            self.done_button.config(state=DISABLED)

            
            
    


            
            



    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        print(card)
        if(card[0] == 'k'):
            self.player_score += 10
        elif(card[0] == 'q'):
            self.player_score += 10
        elif(card[0] == 'j'):
            self.player_score += 10
        elif(card[2] == '_'):
            self.player_score += 10
        else: 
            self.player_score += int(card[0])

        self.score_label.config(text="Your score: " + str(self.player_score) )
        self.score_label.update_idletasks()


        

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        self.closed_deck.config(state=DISABLED)
        self.score_label.config(text="Your score: " + str(self.player_score) + " Well done! Play again?")
        self.score_label.update_idletasks()


    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        self.player_score = 0
        self.score_label.config(text="Your score: " + str(self.player_score))
        self.score_label.update_idletasks()
        the_cards = self.load_cards()

        new_card = the_cards.get()
        new_image = PhotoImage(file=f'Labs\\cards\\{new_card}')
        self.open_card.config(image=new_image)
        self.open_card.photo = new_image
        self.update_score(new_card)

        self.closed_deck.config(state='normal')
        self.done_button.config(state='normal')
        
        
        
        



# object creation here:

app = CardGame()
