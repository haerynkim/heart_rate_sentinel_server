from api import is_tachycardic
import pytest


@pytest.mark.parametrize("candidate, expected", [
    ([0, 128], False),
    ([0, 182], True),
    ([6, 134], True),
    ([22, 128], True),
    ([22, 99], False),
    ([14, 101], False),
    ([9, 120], False)
])
def test_is_tachycardic(candidate, expected):
    """
    This test checks if the heart rate and corresponding age group correctly yields tachycardic diagnosis.
    :param candidate: list
    :param expected: bool
    """
    response = is_tachycardic(candidate[0], candidate[1])
    assert response == expected
