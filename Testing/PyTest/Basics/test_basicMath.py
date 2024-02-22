import pytest
import basicMath

def test_add():
    assert basicMath.add(0, 0) == 0
    assert basicMath.add(1, 5) == 6
    assert basicMath.add(2, 2) == 4
    assert basicMath.add(9, 3) == 12

def test_subtract():
    assert basicMath.subtract(0, 0) == 0
    assert basicMath.subtract(1, 5) == -4
    assert basicMath.subtract(2, 2) == 0
    assert basicMath.subtract(9, 3) == 6

def test_multiply():
    assert basicMath.multiply(0, 0) == 0
    assert basicMath.multiply(1, 5) == 5
    assert basicMath.multiply(2, 2) == 4
    assert basicMath.multiply(9, 3) == 27
    assert basicMath.multiply(2, -3) == -6
    assert basicMath.multiply(-3, -3) == 9
    

def test_divide():
    assert basicMath.divide(1, 5) == 0.2
    assert basicMath.divide(2, 2) == 1
    assert basicMath.divide(9, 3) == 3
    assert basicMath.divide(2, -1) == -2
    assert basicMath.divide(-3, -3) == 1
    assert basicMath.divide(0, 0) == False
    assert basicMath.divide(5, 0) == False
    assert basicMath.divide(0, 10) == 0
