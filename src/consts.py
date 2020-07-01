from dataclasses import dataclass


@dataclass
class Consts:

    latent_length: int = 3
    pre_length: int = 3
    Pd: float = 0.7
    R0: float = 2.0
    K: float = 1/80     # tests per million per day
    positive_tests_percent: float = 1    # represents percentage
    Rl: int = 1

    @property
    def total_length(self):
        return self.latent_length + self.pre_length

    @property
    def daily_R0(self):
        return self.R0 / self.pre_length

    @property
    def chance_to_be_sick(self):
        return self.positive_tests_percent / 100 * self.K * self.total_length

    @property
    def daily_chance_to_be_sick(self):
        return self.positive_tests_percent / 100 * self.K


if __name__ == "__main__":
    defaults = Consts()
    print(defaults)
    non_defaults = Consts(R0=3, Rl=0, Pd=0.8, positive_tests_percent=1)
    print(non_defaults)
