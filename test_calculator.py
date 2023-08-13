import calculator as calculator
import pytest

def assert_fx_equals_y(function,args,ans):
    assert function(args) == int(ans)

def test_minus():
    assert_fx_equals_y(calculator.minus,["6","2"],"4")

def test_divide():
    assert_fx_equals_y(calculator.divide,["6","2"],"3")

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.divide([6,0])

@pytest.mark.parametrize("plus_numbers, plus_expected_result", [
    (["1", "2", "3"], "6"),
    ([2, 7, -10, -4], -5),
    ([-1, 0, 6, -8, 3], 0),
])
def test_plus(plus_numbers, plus_expected_result):
    assert_fx_equals_y(calculator.plus, plus_numbers, plus_expected_result)

@pytest.mark.parametrize("multiply_numbers, multiply_expected_result", [
    (["1", "2", "3"], "6"),
    ([2, 7, -10, -4], 560),
    ([-1, 3, 6, 2, 3], -108),
])
def test_multiply(multiply_numbers, multiply_expected_result):
    assert_fx_equals_y(calculator.multiply, multiply_numbers, multiply_expected_result)