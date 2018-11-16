from api import compile_avg
import pytest

candidate1 = [{"HR": 1}, {"HR": 3}, {"HR": 4}]
expected_list1 = [1, 3, 4]
expected_avg1 = sum(expected_list1) / len(expected_list1)
candidate2 = [{"HR": 5, "Time": 87}, {"HR": 5}]
expected_list2 = [5, 5]
expected_avg2 = 5


@pytest.mark.parametrize("candidate, expected", [
    (candidate1, [expected_list1, expected_avg1]),
    (candidate2, [expected_list2, expected_avg2])
])
def test_compile_avg(candidate, expected):
    list, average = compile_avg(candidate, [])
    assert list == expected[0]
    assert average == expected[1]