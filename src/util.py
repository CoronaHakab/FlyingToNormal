import numpy as np
from typing import Iterable, Union
import math


class ProbabilityVector:
    __slots__ = ("options", "probabilities")

    def __init__(self, options: Union[Iterable, int], probabilities: Iterable[float] = None):
        if type(options) is int:
            self.options = np.arange(1, options + 1)
        else:
            self.options = np.array(options)
        if probabilities is None:
            self.probabilities = np.full_like(self.options, 1 / len(self.options), dtype=float)
        else:
            self.probabilities = np.array(probabilities)
        assert math.isclose(np.sum(self.probabilities), 1.0, abs_tol=1e-3), "total probability must sum to one"
        self.round_last(self.probabilities, 1.0)
        assert len(self.probabilities) == len(self.options), "options and probabilities must be of same length"

    @staticmethod
    def round_last(array: np.ndarray, total_value: float):
        if np.sum(array) != total_value:
            array[-1] = total_value - np.sum(array[:-1])

    def roll(self, shape: int = 1) -> Union[np.ndarray, int]:
        return np.random.choice(self.options, size=shape, p=self.probabilities)

    def max_value(self):
        return max(self.options)

    def min_value(self):
        return min(self.options)

    def str_of_items(self, array: Iterable) -> str:
        ans = ""
        for i in array:
            ans += f" {i},"
        return ans[1:-1]

    def __str__(self):
        return f"options: {self.str_of_items(self.options)}\nprobabilities: {self.str_of_items(self.probabilities)}"


if __name__ == "__main__":
    both_uniform = ProbabilityVector(5)
    print(both_uniform)
    uniform_probability = ProbabilityVector([1, 2, 3, 4])
    print(uniform_probability)
    non_uniform = ProbabilityVector([2, 3, 5], [1/3, 1/3, 1/3])
    print(non_uniform)

    print(non_uniform.roll(10))
