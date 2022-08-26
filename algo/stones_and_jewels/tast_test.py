from algo.stones_and_jewels.task import solution


def test() -> None:
    assert solution("", "") == 0
    assert solution("xyz", "ju2e7z78y2zzxy1") == 6
