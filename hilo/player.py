
class Player:

    def __init__(self):
        #player attributes

        self.points = 300
        

    def make_guess(self):
        guess = input("Higher or Lower? [h/l]")
        return guess
        
        
    def add_or_sub_points(self, correct):

        if correct:
            self.points = self.points + 100
        else:
            self.points = self.points - 75
        points = self.points
        return points
    
    def can_play(self):
        
        if self.points > 0:
            return self.play_again()
        else:
            print("Tha-the-that..that's all folks")
            return False

    def play_again(self):
        answer = input("Do you want to play again? (Y/N) ")
        if answer == "Y":
            
            return True

        else:
            print("Tha-the-that..that's all folks")
            
            return False
 