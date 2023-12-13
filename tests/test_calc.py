import pytest

from calc import Calculator


def test_calculator_init_valid_params():
    a = 5
    b = 2
    calc = Calculator(a, b)

    assert calc.get_a() == a
    assert calc.get_b() == b


def test_calculator_init_invalid_param_a():
    a = "3"
    b = 4

    with pytest.raises(ValueError):
        Calculator(a, b)


def test_calculator_init_invalid_param_b():
    a = 0
    b = "a"

    with pytest.raises(ValueError):
        Calculator(a, b)


def test_calculator_operation_add():
    a = 9
    b = -3
    expected_result = a + b
    c = Calculator(a, b)

    assert c.addition == expected_result


def test_calculator_operation_mult():
    a = -1
    b = 33
    c = Calculator(a, b)
    expected_result = a * b

    assert c.multiplication == expected_result


def test_calculator_operation_sub():
    a = 14
    b = 4
    c = Calculator(a, b)
    expected_result = a - b

    assert c.subtraction == expected_result


def test_calculator_operation_div():
    a = -4
    b = 8
    c = Calculator(a, b)
    expected_result = a / b

    assert c.division == expected_result


def test_calculator_zero_division():
    a = 10
    b = 0
    c = Calculator(a, b)
    with pytest.raises(ZeroDivisionError):
        c.division


def test_calculator_str():
    a = 3
    b = 5
    calc = Calculator(a, b)
    expected_str = f"{a = }, {b = }"

    assert str(calc) == expected_str
