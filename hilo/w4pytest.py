import pytest 

from dealer import Dealer
from player import Player

#check to see if the functions work
dealer = Dealer()
player = Player()

def test_is_guess_correct():
    #tests if given certain parameters, the right booleans are returned
    assert dealer.is_guess_correct('h', 7, 10) == True
    assert dealer.is_guess_correct('h', 10, 7) == False
    assert dealer.is_guess_correct('l', 10, 7) == True
    assert dealer.is_guess_correct('l', 7, 10) == False

def test_add_or_sub_points():
    #tests to see if the points are actually added or subtracted
    testPoints = 300
    player.points = testPoints
    assert player.add_or_sub_points(True) == testPoints + 100
    player.points = testPoints
    assert player.add_or_sub_points(False) == testPoints - 75
    

pytest.main(["-v", "--tb=no", "w4pytest.py"])

