import numpy as np
import pytest

from testrepocomputing.square_bin import square_bin

def test_numbers():
    """Test the square_bin function with numbers.

    Note in principle we have to test integers and floating points separately.
    As documented in the underlying function, the output is always expected to
    be a floating point.
    """
    assert square_bin(2, 3) == 25.
    assert square_bin(2., 3.) == 25.
    assert square_bin(2, -3) == 1.
    assert square_bin(2., -3.) == 1.
    assert square_bin(-2, -3) == 25.
    assert square_bin(-2., -3.) == 25.
    assert square_bin(-2, 3) == 1.
    assert square_bin(-2., 3.) == 1.


def test_string():
    """Calling square() with a string as the argument should raise TypeError.
    """
    with pytest.raises(TypeError) as exception:
        square_bin('hello', 'world')
    print(f'Caught exception {exception}')    