# The conftest.py file serves as a means of providing fixtures for an entire directory. 
# Fixtures defined in a conftest.py can be used by any test in that package without needing to import them (pytest will automatically discover them).

import Shapes
import pytest

@pytest.fixture
def small_rectangle():
    return Shapes.Rectangle(1,1)