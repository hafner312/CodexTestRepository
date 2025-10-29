import pytest

from codex_demo.fibonacci import FibonacciResult, fibonacci


def test_fibonacci_zero():
    result = fibonacci(0)
    assert result == FibonacciResult(n=0, value=0, sequence=(0,))


def test_fibonacci_sequence():
    result = fibonacci(7)
    assert result.value == 13
    assert result.sequence == (0, 1, 1, 2, 3, 5, 8, 13)


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)
