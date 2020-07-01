from medical import MedicalState
from util import ProbabilityVector
import numpy as np


class Agent:
    __slots__ = (
        "medical_state",
        "days_left_in_state"
    )

    def __init__(self, medical_state: MedicalState):
        self.medical_state: MedicalState = medical_state
        self.days_left_in_state: int = medical_state.roll_length()
        self.test_for_state_transition()

    def test_for_state_transition(self) -> bool:
        if self.days_left_in_state > 0:
            return False
        while self.days_left_in_state == 0:
            self.medical_state = self.medical_state.next_state
            if self.medical_state is None:
                break
            self.days_left_in_state = self.medical_state.roll_length()
        return True

    def perform_test(self) -> bool:
        return np.random.random() < self.medical_state.tests_pd[-self.days_left_in_state]

    def r_factor(self) -> float:
        return self.medical_state.contagious_factor[-self.days_left_in_state]

    def advance_day(self) -> bool:
        self.days_left_in_state -= 1
        return self.test_for_state_transition()
