from api import parse
import pytest

@pytest.mark.parametrize("candidate, expected", [
    ([{"candy":['snickers','oreos','gummies']}, "candy"], ['snickers','oreos','gummies']),
    ([{"age":32, "race":"Asian"}, "age"], 32)
])

def test_parse(candidate, expected):
    assert parse(candidate[0], candidate[1]) == expected