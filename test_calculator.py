import pytest

from unittest.mock import patch

from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)

# ─── add_numbers ───────────────────────────────────────────


def test_add_positive_numbers():

    assert add_numbers(10, 5) == 15


def test_add_negative_numbers():

    assert add_numbers(-10, -5) == -15


def test_add_zero():

    assert add_numbers(0, 5) == 5


def test_add_floats():

    assert add_numbers(1.5, 2.5) == 4.0


# ─── subtract_numbers ──────────────────────────────────────


def test_subtract_positive_numbers():

    assert subtract_numbers(10, 5) == 5


def test_subtract_negative_result():

    assert subtract_numbers(5, 10) == -5


def test_subtract_zero():

    assert subtract_numbers(5, 0) == 5


def test_subtract_floats():

    assert subtract_numbers(10.5, 0.5) == 10.0


# ─── multiply_numbers ──────────────────────────────────────


def test_multiply_positive_numbers():

    assert multiply_numbers(10, 5) == 50


def test_multiply_by_zero():

    assert multiply_numbers(10, 0) == 0


def test_multiply_negative_numbers():

    assert multiply_numbers(-3, 4) == -12


def test_multiply_floats():

    assert multiply_numbers(2.5, 4) == 10.0


# ─── divide_numbers ────────────────────────────────────────


def test_divide_positive_numbers():

    assert divide_numbers(10, 5) == 2.0


def test_divide_negative_numbers():

    assert divide_numbers(-10, 2) == -5.0


def test_divide_float_result():

    assert divide_numbers(10, 3) == pytest.approx(3.333, rel=1e-3)


def test_divide_by_zero_returns_string():

    # your code returns a string, not raises exception

    assert divide_numbers(10, 0) == "Error: Division by zero"


def test_divide_by_zero_return_type():

    # confirms it returns a string, not a number

    result = divide_numbers(10, 0)

    assert isinstance(result, str)


# ─── main() input handling ─────────────────────────────────


def test_main_addition(capsys):
    """Test full flow: 10 + 5 = 15"""

    with patch("builtins.input", side_effect=["10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 15" in captured.out


def test_main_subtraction(capsys):
    """Test full flow: 10 - 5 = 5"""

    with patch("builtins.input", side_effect=["10", "5", "-"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 5" in captured.out


def test_main_multiplication(capsys):
    """Test full flow: 10 * 5 = 50"""

    with patch("builtins.input", side_effect=["10", "5", "*"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 50" in captured.out


def test_main_division(capsys):
    """Test full flow: 10 / 5 = 2"""

    with patch("builtins.input", side_effect=["10", "5", "/"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Result: 2" in captured.out


def test_main_invalid_first_number(capsys):
    """Alphabet as first input is rejected, then accepts valid number."""

    with patch("builtins.input", side_effect=["abc", "10", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out

    assert "Result: 15" in captured.out


def test_main_invalid_second_number(capsys):
    """Alphabet as second input is rejected, then accepts valid number."""

    with patch("builtins.input", side_effect=["10", "abc", "5", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out

    assert "Result: 15" in captured.out


def test_main_invalid_operation(capsys):
    """Invalid operation is rejected, then accepts valid one."""

    with patch("builtins.input", side_effect=["10", "5", "x", "+"]):

        from calculator import main

        main()

    captured = capsys.readouterr()

    assert "Invalid operation" in captured.out

    assert "Result: 15" in captured.out
