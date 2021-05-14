from dealer import Dealer
from player import Player

'''Dealer class

random card 1-13

displays current card

shows next card

if points hit 0 game over takes points as a parameter return can play

if can play ask user if they want to play again

'''

'''Player class

starts with 300 points

takes current card as parameter and asks if it will be higher or lower

current card, user input and next card as parameters determine if player was right return True or False

takes boolean as parameter and either adds or subtracts points

return points
'''



def main():

    dealer = Dealer()
    player = Player()

    keep_playing = True

    while keep_playing == True:

        first_card = dealer.display_card()

        guess = player.make_guess()

        next_card = dealer.display_card()

        correct = dealer.is_guess_correct(guess, first_card, next_card)

        player.add_or_sub_points(correct)

        print("")
        print(f"You now have {player.points} points.")
        print("")

        keep_playing = player.can_play()


main()
        

