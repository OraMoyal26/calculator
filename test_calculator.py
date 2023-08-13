import calculator as calculator
import pytest

def test_plus():
    assert_fx_equals_y(calculator.plus,6,2,8)

def test_minus():
    assert_fx_equals_y(calculator.minus,6,2,4)

def test_multiply():
    assert_fx_equals_y(calculator.multiply,6,2,12)

def test_divide():
    assert_fx_equals_y(calculator.divide,6,2,3)

def assert_fx_equals_y(f, x, y,ans):
    assert f(x,y) == ans

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.divide(6, 0)
