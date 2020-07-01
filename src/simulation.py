from src.consts import Consts
from src.tests_policy import TestPolicies
import numpy as np


class Simulation:
    __slots__ = ("consts",
                 "tests_policy",
                 "array",
                 "infected",
                 "people",
                 "initial_patients",
                 "is_stochastic")

    def __init__(self, consts: Consts, tests_policy: TestPolicies, people: int, is_stochastic: bool = True):
        # initialize things
        self.consts = consts
        self.tests_policy = tests_policy
        self.infected = 0
        self.people = people
        self.is_stochastic = is_stochastic

        # run simulation
        self.fill_array()
        self.run_days()

    def fill_array(self):
        # initialize array
        if self.is_stochastic:
            sick_rolls = np.random.random(self.people)
            sick_amount = np.count_nonzero((sick_rolls <= self.consts.chance_to_be_sick))
            day_rolls = np.random.randint(0, self.consts.total_length, sick_amount)
            self.array = np.bincount(day_rolls, minlength=self.consts.total_length)
        else:
            sick_amount = self.people * self.consts.chance_to_be_sick
            self.array = np.array([sick_amount / self.consts.total_length] * self.consts.total_length)

        if -1 in self.tests_policy.value:
            self.perform_tests()
        self.initial_patients = sum(self.array)

    def run_days(self):
        for i in range(self.consts.total_length):
            # perform tests
            if (i+1) in self.tests_policy.value:
                self.perform_tests()
            # count infections
            self.count_new_infected()
            # progress day
            for index in range(1, len(self.array)):
                self.array[-index] = self.array[-index - 1]
            self.array[0] = 0

    # todo use daily Pd
    def perform_tests(self):
        for index in range(len(self.array)):
            if self.is_stochastic:
                rolls = np.random.random(self.array[index])
                self.array[index] = np.count_nonzero(rolls <= self.consts.Pd)
            else:
                self.array[index] *= self.consts.Pd

    def count_new_infected(self):
        for index in range(self.consts.pre_length):
            self.infected += self.consts.daily_R0 * self.array[-index - 1]

    def __str__(self):
        return f"consts: {self.consts} \ntests policy: {self.tests_policy}\n" \
               f"initial patients: {self.initial_patients}, first circle infections: {self.infected}"
