import random

class Dealer:

    def display_card(self):
        #calls the get card function and shows the first card and returns it
        current_card = self.get_card()
        print(f"Dealt card: {current_card}")
        return current_card

    def get_card(self):
        # gets a random card for the display card function
        card = random.randint(1, 13)
        return card

    def is_guess_correct(self, guess, first_card, next_card):
        #takes the first card and the second card and compares them to see if the guess was right
        if guess == "h" and first_card < next_card:
            return True
        elif guess == "l" and first_card > next_card:
            return True
       #if it's wrong return False
        else:
            return False


