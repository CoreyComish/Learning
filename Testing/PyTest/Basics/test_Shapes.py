import Shapes
import pytest
import math

# Classed Based Testing
class TestCircle:

    def setup_method(self, test_method):
        print(f"Setting up {test_method}")
        self.circle = Shapes.Circle(10)

    def teardown_method(self, test_method):
        print(f"Tearing down {test_method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

#Functional Testing, with Fixtures
        
@pytest.fixture
def my_rectangle():
    return Shapes.Rectangle(10, 10)

@pytest.fixture
def other_rectangle():
    return Shapes.Rectangle(2, 99)

def test_area(my_rectangle):
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.width

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (my_rectangle.length + my_rectangle.width)

def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle

def test_not_equal_2(my_rectangle, small_rectangle):
    assert small_rectangle != my_rectangle