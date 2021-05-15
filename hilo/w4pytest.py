import pytest 

from dealer import is_guess_correct
from player import add_or_sub_points

#check to see if the functions work

def validate_is_guess_correct():
    
    assert is_guess_correct(h, 7, 10) == True
    assert is_guess_correct(h, 10, 7) == False
    assert is_guess_correct(l, 10, 7) == True
    assert is_guess_correct(l, 7, 10) == False

def validate_add_or_sub_points():
    points = 100
    assert add_or_sub_points(True) == points + 100
    assert add_or_sub_points(False) == points - 75
    

pytest.main(["-v", "--tb=no", "test_w4pytest.py"])

