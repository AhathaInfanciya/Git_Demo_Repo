from unittest.mock import patch

from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    main,
)


def test_add_numbers():
    assert add_numbers(10, 5) == 15


def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5


def test_multiply_numbers():
    assert multiply_numbers(10, 5) == 50


def test_divide_numbers():
    assert divide_numbers(10, 5) == 2


def test_divide_by_zero():
    assert divide_numbers(10, 0) == "Error: Division by zero"


def test_main_add_operation(capsys):
    with patch("builtins.input", side_effect=["3", "4", "+"]):
        main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: 7"


def test_main_subtract_operation(capsys):
    with patch("builtins.input", side_effect=["10", "4", "-"]):
        main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: 6"


def test_main_multiply_operation(capsys):
    with patch("builtins.input", side_effect=["6", "7", "*"]):
        main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: 42"


def test_main_divide_operation(capsys):
    with patch("builtins.input", side_effect=["10", "5", "/"]):
        main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: 2"


def test_main_divide_by_zero_prints_error(capsys):
    with patch("builtins.input", side_effect=["10", "0", "/"]):
        main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: Error: Division by zero"


def test_main_invalid_operation(capsys):
    with patch("builtins.input", side_effect=["1", "2", "x", "+"]):
        main()

    out = capsys.readouterr().out.strip()

    assert "Invalid operation" in out
    assert "Result: 3" in out