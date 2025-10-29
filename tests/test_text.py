import pytest

from codex_demo.text import WordStatistics, word_statistics


def test_word_statistics_basic():
    text = "Hallo Welt hallo"
    result = word_statistics(text)
    assert result == WordStatistics(word_count=3, unique_word_count=2, most_common=("hallo", 2))


def test_word_statistics_empty():
    result = word_statistics("")
    assert result.word_count == 0
    assert result.unique_word_count == 0
    assert result.most_common is None


def test_word_statistics_type_error():
    with pytest.raises(TypeError):
        word_statistics(None)  # type: ignore[arg-type]
