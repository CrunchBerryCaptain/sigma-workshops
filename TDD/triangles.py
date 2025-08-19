def is_valid_triangle(angles: list[int]) -> bool:

    if len(angles) != 3:
        return False

    if sum(angles) != 180:
        return False

    return True


def is_valid_equilateral_triangle(angles: list[int]) -> bool:
    """Returns True if angles form a valid equilateral triangle"""
    pass


def get_triangle_type(angles: list[int]) -> bool:
    """Returns type of triangle based off angles
    isosceles, right-angle, equilateral, scalene"""
    pass
