
class Player:

    def __init__(self):
        #player attributes

        self.points = 300
        

    def make_guess(self):
        #gets guess from user
        guess = input("Higher or Lower? [h/l]")
        return guess
        
        
    def add_or_sub_points(self, correct):
        #takes the right or wrong guess and either adds or subtracts points
        if correct:
            self.points = self.points + 100
        else:
            self.points = self.points - 75
        points = self.points
        return points
    
    def can_play(self):
        #sees if player still has points, if yes calls the play again method
        if self.points > 0:
            return self.play_again()
        #if player doesn't, end game
        else:
            print("Tha-the-that..that's all folks")
            return False

    def play_again(self):
        #asks player if they want to play again
        answer = input("Do you want to play again? (Y/N) ")
        if answer == "Y":
            
            return True
        #if player doesn't want to play again, end game
        else:
            print("Tha-the-that..that's all folks")
            
            return False
 