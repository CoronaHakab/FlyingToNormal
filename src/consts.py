from dataclasses import dataclass
from util import ProbabilityVector
from medical import MedicalState, latent, pre_symptomatic


@dataclass
class Consts:

    latent_state: MedicalState = latent
    pre_symptomatic_state: MedicalState = pre_symptomatic
    # symptomatic_state
    Pd: float = 0.7
    R0: float = 2.0
    K: float = 1/80     # tests per million per day
    positive_tests_percent: float = 1    # represents percentage
    Rl: int = 1

    @property
    def maximum_length_till_symptoms(self):
        return self.latent_state.max_length + self.pre_symptomatic_state.max_length

    @property
    def daily_chance_to_be_sick(self):
        return self.positive_tests_percent / 100 * self.K


if __name__ == "__main__":
    defaults = Consts()
    print(defaults)
    non_defaults = Consts(R0=3, Rl=0, Pd=0.8, positive_tests_percent=1)
    print(non_defaults)
