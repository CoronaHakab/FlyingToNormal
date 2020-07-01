import numpy as np
from typing import List, Set

from src.consts import Consts
from src.tests_policy import TestPolicies
from agent import Agent
from medical import MedicalState
from util import ProbabilityVector


class Simulation:
    __slots__ = ("consts",
                 "tests_policy",
                 "agents",
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
        self.agents: Set[Agent] = set()

        # run simulation
        self.fill_array()
        self.run_days()

    def fill_array(self):
        # initialize array
        for day in range(self.consts.maximum_length_till_symptoms):
            new_agents: Set[Agent] = set()
            for _ in range(round(self.consts.daily_chance_to_be_sick * self.people)):
                agent = Agent(self.consts.latent_state)
                if agent.advance_days(day) and agent.medical_state.name != "symptomatic":
                    new_agents.add(agent)
            self.agents.update(new_agents)

        # check if was tested before flight. if so, reduces number of agents
        if -1 in self.tests_policy.value:
            self.perform_tests()
        self.initial_patients = len(self.agents)

    def run_days(self):
        days_since_landing = 1
        while len(self.agents) > 0:
            # perform tests
            if days_since_landing in self.tests_policy.value:
                self.perform_tests()

            # count infections
            self.count_new_infected()

            # progress day
            agents_to_remove = set()
            for agent in self.agents:
                if not agent.advance_days():
                    agents_to_remove.add(agent)
            self.agents.difference_update(agents_to_remove)

            days_since_landing += 1

    def perform_tests(self):
        agents_to_remove: Set[Agent] = set()
        for agent in self.agents:
            if agent.perform_test():
                agents_to_remove.add(agent)
        self.agents.difference_update(agents_to_remove)

    def count_new_infected(self):
        for agent in self.agents:
            self.infected += agent.r_factor() * self.consts.R0

    def __str__(self):
        return f"consts: {self.consts} \ntests policy: {self.tests_policy}\n" \
               f"initial patients: {self.initial_patients}, first circle infections: {self.infected}"
