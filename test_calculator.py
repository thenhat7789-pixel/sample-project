from calculator import multiply, is_positive
import pytest

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_with_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_is_positive_true():
    assert is_positive(5) == True

def test_is_positive_false():
    assert is_positive(-5) == False

def test_is_positive_zero_raises_error():
    with pytest.raises(ValueError):
        is_positive(0)
