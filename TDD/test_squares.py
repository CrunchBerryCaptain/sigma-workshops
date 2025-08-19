"""Test for functions in squares.py file"""

from squares import is_valid_square


def test_is_valid_square_valid_true_1():

    # Arrange
    data = [1, 1, 1, 1]

    # Act
    result = is_valid_square(data)

    # Assert
    assert result == True


def test_is_valid_square_valid_true_2():

    # Arrange, Act, Assert
    assert is_valid_square([4, 4, 4, 4]) == True


def test_is_valid_square_valid_false_1():

    data = [1, 2, 3, 4]
    result = is_valid_square(data)
    assert result == False


def test_is_valid_square_valid_false_2():

    data = [1, 2, 3]
    result = is_valid_square(data)
    assert result == False
