from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers
)

def test_add_numbers():
    assert add_numbers(10, 5) == 15

def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5

def test_multiply_numbers():
    assert multiply_numbers(10, 5) == 50

def test_divide_numbers():
    assert divide_numbers(10, 5) == 2.0

def test_divide_by_zero():
    assert divide_numbers(10, 0) == "Error: Division by zero"