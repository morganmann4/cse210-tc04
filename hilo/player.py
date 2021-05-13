#import Morgan's class
from dealer.py import Dealer

class Player:

    def __init__(self):
        #player attributes

        self.points = 300

    def make_guess(self):
        guess = input("Enter higher or lower")
        return guess
        

    def add_or_sub_points(self, correct):

        if correct == True:
            self.points = self.points + 100
        else:
            self.points = self.points - 75

    def get_points(self):
        return self.points  