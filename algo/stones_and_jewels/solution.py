def solution(jewels: str, stones: str) -> int:
    result = sum(stone in jewels for stone in stones)

    return result
