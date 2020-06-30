from src.consts import Consts
from src.tests_policy import TestPolicies


class Simulation:
    __slots__ = ("consts",
                 "tests_policy",
                 "array",
                 "infected",
                 "people",
                 "initial_patients")

    def __init__(self, consts: Consts, tests_policy: TestPolicies, people: int):
        self.consts = consts
        self.tests_policy = tests_policy
        self.infected = 0
        self.people = people
        self.fill_array()
        self.run_days()

    def fill_array(self):
        sick_amount = self.people * self.consts.Pi
        if -1 in self.tests_policy.value:
            sick_amount *= (1 - self.consts.Pd)
        self.array = [sick_amount / self.consts.total_length] * self.consts.total_length
        self.initial_patients = sum(self.array)

    def run_days(self):
        for i in range(self.consts.total_length):
            # perform tests
            if (i+1) in self.tests_policy.value:
                for j in range(len(self.array)):
                    self.array[j] = self.array[j] * (1 - self.consts.Pd)

            for index in range(self.consts.pre_length):
                self.infected += self.consts.daily_R0 * self.array[-index - 1]
            self.array[0] = 0
            for index in range(1, len(self.array)):
                self.array[-index] = self.array[-index - 1]

    def __str__(self):
        return f"consts: {self.consts} \ntests policy: {self.tests_policy}\n" \
               f"initial patients: {self.initial_patients}, first circle infections: {self.infected}"
