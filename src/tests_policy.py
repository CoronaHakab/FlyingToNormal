from enum import Enum


class TestPolicies(Enum):
    GREEN = []
    YELLOW = [1]
    ORANGE = [-1, 1, 7, 14]
    RED = [-1, 1, 4, 7, 11, 14]
