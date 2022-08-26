import pytest

from algo.max_len_seq.solution import get_len


@pytest.mark.parametrize(
    "string,length",
    (
        ("", 0),
        ("a", 1),
        ("aaaa", 4),
        ("aaab", 3),
        ("aaabbb", 3),
        ("aabbbccaabb", 3),
        ("abbbaabbb", 3),
        ("abbc", 2),
        ("baaa", 3),
    ),
)
def test_empty(string: str, length: int) -> None:
    assert get_len(string) == length
