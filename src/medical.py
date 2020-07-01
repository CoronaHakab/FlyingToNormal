from typing import Union, Sequence, Any
from dataclasses import dataclass, field
from util import ProbabilityVector
import numpy as np


@dataclass
class MedicalState:

    name: str
    length_pv: ProbabilityVector
    contagious_factor: Union[Sequence, float]
    tests_pd: Union[Sequence, float]
    next_state: Any = None
    self_quarantine_chance: float = 0.0  # chance to self-quarantine (if hsa symptoms) between 0 - 1

    def __post_init__(self):
        if type(self.contagious_factor) is float or type(self.contagious_factor) is int:
            self.contagious_factor = [self.contagious_factor] * self.max_length
        if type(self.tests_pd) is float or type(self.tests_pd) is int:
            self.tests_pd = [self.tests_pd] * self.max_length

        assert self.max_length <= len(self.contagious_factor), "length is larger than contagious vector"
        assert self.max_length <= len(self.tests_pd), "length is larger than tests pd vector"

    @property
    def min_length(self) -> int:
        return self.length_pv.min_value()

    @property
    def max_length(self) -> int:
        return self.length_pv.max_value()

    def roll_length(self) -> int:
        return self.length_pv.roll()[0]


symptomatic_length_pv = ProbabilityVector([7], [1.0])
symptomatic_contagious_factor = [0.218, 0.157, 0.109, 0.073, 0.048, 0.036, 0.024, 0.012]
symptomatic = MedicalState(name="symptomatic", length_pv=symptomatic_length_pv, next_state=None,
                           contagious_factor=symptomatic_contagious_factor, tests_pd=0.99, self_quarantine_chance=1.0)

pre_symptomatic_length_pv = ProbabilityVector(np.arange(4))
pre_symptomatic = MedicalState(name="pre-symptomatic", length_pv=pre_symptomatic_length_pv, contagious_factor=0.34,
                               tests_pd=0.95, next_state=symptomatic)

latent_length_pv = ProbabilityVector(13, [0.083, 0.13325, 0.16925, 0.169, 0.144,
                                          0.10675, 0.0725, 0.04675, 0.02925, 0.021, 0.01275, 0.00775, 0.00475])
latent = MedicalState(name="latent", length_pv=latent_length_pv, contagious_factor=0, tests_pd=0.6,
                      next_state=pre_symptomatic)
