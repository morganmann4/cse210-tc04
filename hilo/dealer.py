import random
from player.py import Player

class Dealer:

    def __init__(self):
        #Player attributes
        self.keep_playing = True
        self.player = Player()
        self.cards = []
        self.score = 300
        


    def start_game(self):
        #start the game and keep the game running
        while self.keep_playing:
            self.get_cards()
            self.guess()
            self.check_guess()
            self.evaluate_score()
            self.can_play()
            self.check_if_game_still_going()
            

    
    def get_cards(self):
        #creates a list of two cards
        self.cards.clear()
        for i in range(2):
            result = random.randint(1, 13)
            self.cards.append(result)

        
     
    def guess(self):
        #Shows the cards and takes players guess
        print("The card is: {card[0]}")
        self.guess = self.player.make_guess()
        print("The next card was: {card[1]}")


    def check_guess(self):
        # Checks to see if the guess was right or not
        if card[0] > card[1] and self.guess == "h" or card[0] < card[1] and self.guess == "l":
            return True

        else:
            return False

    def evaluate_score(self):
        #determines the new score
        self.score = self.player.add_or_subtract_points()
        print("Your score is: {self.score}")

    def can_play():
        #checks to see if the score has reached 0
        if self.score == 0:
            return True
        else:
            return False

        
    def check_if_game_still_going(self):  
        #If the player has more than zero then the player can decide if they want to continue playing
        if can_play():
            choice = input("Keep playing? [y/n]")
            self.keep_playing = (choice == y)
            
        else:
            keep_playing = False

