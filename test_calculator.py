import pytest
from calculator import divide

def test_divide_returns_float():
    assert divide(3, 2) == 1.5

def test_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
