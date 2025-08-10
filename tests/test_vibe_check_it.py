import pytest
from vibe_check_it import vibe_check_it
from dotenv import load_dotenv

load_dotenv()

def vibesort(items):
    return sorted(items, key=str)

def buggy_vibesort(items):
    return items

def vibeisodd(number):
    return number % 2 == 1

def buggy_vibeisodd(number):
    return not number % 2 == 1

@pytest.mark.parametrize("func, input_data, expected", [
    (vibesort, ["banana", "apple", "cherry"], True),
    (vibesort, [2,3,4,1], True),
    (buggy_vibesort, ["banana", "apple", "cherry"], False),
    (buggy_vibesort, [2,3,4,1], False),
    (vibeisodd, 5, True),
    (vibeisodd, 6, True),
    (buggy_vibeisodd, 5, False),
])
def test_are_you_sure(func, input_data, expected):
    assert vibe_check_it(func, input_data) == expected

