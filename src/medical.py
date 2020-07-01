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

    def __post_init__(self):
        if type(self.contagious_factor) is float:
            self.contagious_factor = [self.contagious_factor] * self.max_length
        if type(self.tests_pd) is float:
            self.tests_pd = [self.tests_pd] * self.max_length

        assert self.max_length <= len(self.contagious_factor), "length is larger than contagious vector"
        assert self.max_length <= len(self.tests_pd), "length is larger than tests pd vector"

    @property
    def min_length(self) -> int:
        return self.length_pv.min_value()

    @property
    def max_length(self) -> int:
        return self.length_pv.max_value()


# todo add this
# symptomatic_length_pv = ProbabilityVector(np.arrange())
# symptomatic = MedicalState()...

pre_symptomatic_length_pv = ProbabilityVector(np.arrange(4))
pre_symptomatic = MedicalState(name="pre-symptomatic", length_pv=pre_symptomatic_length_pv, contagious_factor=0.25, tests_pd=0.9, next_state=None)

latent_length_pv = ProbabilityVector([13], [0.083, 0.13325, 0.16925, 0.169, 0.144, 0.10675, 0.0725, 0.04675, 0.02925, 0.021, 0.01275, 0.00775, 0.00475])
latent = MedicalState(name="latent", length_pv=latent_length_pv, contagious_factor=0, tests_pd=0.5, next_state=pre_symptomatic)
