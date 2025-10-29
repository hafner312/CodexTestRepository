"""Fibonacci Werkzeuge."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class FibonacciResult:
    """Ergebniscontainer für die Fibonacci-Berechnung."""

    n: int
    value: int
    sequence: tuple[int, ...]


@lru_cache(maxsize=None)
def fibonacci_number(n: int) -> int:
    """Berechnet die n-te Fibonacci Zahl mit Memoisierung."""
    if n < 0:
        raise ValueError("n darf nicht negativ sein")
    if n in {0, 1}:
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci(n: int) -> FibonacciResult:
    """Gibt den Wert und die Folge bis n zurück."""
    if n < 0:
        raise ValueError("n darf nicht negativ sein")
    sequence = tuple(fibonacci_number(i) for i in range(n + 1))
    return FibonacciResult(n=n, value=sequence[-1], sequence=sequence)
