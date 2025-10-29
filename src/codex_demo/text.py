"""Text-Analysen."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class WordStatistics:
    """Statistiken für Textinhalte."""

    word_count: int
    unique_word_count: int
    most_common: tuple[str, int] | None


def _tokenize(words: Iterable[str]) -> list[str]:
    return [word.lower() for word in words if word]


def word_statistics(text: str) -> WordStatistics:
    """Berechnet Wortstatistiken für den gegebenen Text."""
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    tokens = _tokenize(text.split())
    counter = Counter(tokens)
    most_common = counter.most_common(1)
    return WordStatistics(
        word_count=len(tokens),
        unique_word_count=len(counter),
        most_common=most_common[0] if most_common else None,
    )
