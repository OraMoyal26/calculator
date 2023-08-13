import calculator as calculator

def test_plus():
    assert_fx_equals_y(calculator.plus,6,2,8)

def test_minus():
    assert_fx_equals_y(calculator.minus,6,2,4)

def test_multiply():
    assert_fx_equals_y(calculator.multiply,6,2,12)

def test_division():
    assert_fx_equals_y(calculator.division,6,2,3)

def assert_fx_equals_y(f, x, y,ans):
    assert f(x,y) == ans
