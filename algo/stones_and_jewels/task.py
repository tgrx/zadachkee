def solution(jewels: str, stones: str) -> int:
    """
    Даны две строки строчных латинских символов:
    строка J и строка S.

    Символы, входящие в строку J, — «драгоценности»,
    входящие в строку S — «камни».

    Нужно определить,
    какое количество символов из S
    одновременно являются «драгоценностями».

    Проще говоря, нужно проверить,
    какое количество символов из S входит в J.
    """
    result = sum(stone in jewels for stone in stones)

    return result
