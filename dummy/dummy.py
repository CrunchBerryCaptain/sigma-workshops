from unittest.mock import patch
from person import get_person


@patch('person.get_name', return_value='Tester Name')
@patch('person.get_age', return_value=999)
def test_get_person(mock_get_name, mock_get_age):
    """Tests the get_person function."""

    # Call the function
    person = get_person()

    # Check the result
    assert person == {
        "name": "Tester Name",
        "age": 999
    }
