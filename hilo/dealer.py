import random

class Dealer:

    def display_card(self):
        current_card = self.get_card()
        print(f"Dealt card: {current_card}")
        return current_card

    def get_card(self):
        card = random.randint(1, 13)
        return card

    def is_guess_correct(self, guess, first_card, next_card):
        if guess == "h" and first_card < next_card:
            return True
        elif guess == "l" and first_card > next_card:
            return True
        else:
            return False


