from math_utils import *

def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(-3) == 9

def test_triplo():
    assert triplo(3) == 8


def test_cubo():
    assert cubo(2) == 8
    assert cubo(-3) == -27
    
def test_is_int():
    assert is_int(2) == True
    assert is_int(2.1) == False
    assert is_int([2]) == False
    assert is_int([2,3]) == False
    assert is_int("1") == False
    assert is_int((2)) == False
    assert is_int((2,3)) == False