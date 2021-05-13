from dealer.py import Dealer

class Player:

    def __init__(self):
        #player attributes

        self.points = 300
        self.guess = None
        self.dealer = Dealer()

    def make_guess(self):
        self.guess = input("Higher or Lower? [h/l]")
        return guess
        
        
    def add_or_sub_points(self):

        if self.dealer.check_guess():
            self.points = self.points + 100
        else:
            self.points = self.points - 75
        return points

    def get_points(self):
        return self.points  
