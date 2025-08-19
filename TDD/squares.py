"""Functions to handle squares"""


def is_valid_square(sides: list[int]) -> bool:

    result = len(set(sides))
    if result != 1:
        return False

    return True
