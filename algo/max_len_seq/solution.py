def get_len(string: str) -> int:
    current_maximum = 0
    maximum = 0
    previous_char = ""

    for current_char in string:
        if current_char == previous_char:
            current_maximum += 1
        else:
            current_maximum = 1

        maximum = max(maximum, current_maximum)
        previous_char = current_char

    return maximum
