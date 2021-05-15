from dealer import Dealer
from player import Player

#outline for code

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
    #loops through methods until player doesn't want to play or has no more points
    while keep_playing == True:
        #calls the display card funtion that calls the get card function
        first_card = dealer.display_card()
        #gets the guess from the player returns to the "guess" variable
        guess = player.make_guess()
        #dealer shows the next card by calling the display card function again returns to the "next_card" variable
        next_card = dealer.display_card()
        #takes the players guess, the first card and second card and sees if player is right returns it to the "correct" variable
        correct = dealer.is_guess_correct(guess, first_card, next_card)
        #gets the points
        player.add_or_sub_points(correct)
        #prints the points
        print("")
        print(f"You now have {player.points} points.")
        print("")
        #sees if the player can or wants to keep playing
        keep_playing = player.can_play()

#calls the main function to start it all
main()
        

