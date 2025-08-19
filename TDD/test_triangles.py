from triangles import is_valid_triangle, is_valid_equilateral_triangle, get_triangle_type


def test_is_valid_triangle_valid_true_1():

    angles = [60, 60, 60]
    result = is_valid_triangle(angles)
    assert result == True


def test_is_valid_triangle_valid_true_2():

    angles = [30, 30, 120]
    result = is_valid_triangle(angles)
    assert result == True


def test_is_valid_triangle_valid_false_1():

    angles = [1, 1, 1]
    result = is_valid_triangle(angles)
    assert result == False


def test_is_valid_triangle_valid_false_2():

    angles = [180]
    result = is_valid_triangle(angles)
    assert result == False


def test_is_valid_triangle_valid_false_3():

    angles = [0, 0, 0]
    result = is_valid_triangle(angles)
    assert result == False
