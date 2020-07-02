from src.consts import Consts
from src.tests_policy import TestPolicies
from src.simulation import Simulation
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def print_categories_boundaries(people_per_simulation: int = 100_000, R0_low: float = 1.0, R0_high: float = 3,
                                is_stochastic: bool = True):
    print("\nprinting categories boundaries:\n")

    def print_color_range(color: str, low_simulation: Simulation, high_simulation: Simulation):
        print(f"\ncategory {color} boundaries:\n"
              f"incoming sicks: \t {low_simulation.initial_patients} - {high_simulation.initial_patients}\n"
              f"first circles infections: \t {low_simulation.infected} - {high_simulation.infected}")

    # green
    min_percent = 0
    max_percent = 1
    green_min_consts = Consts(positive_tests_percent=min_percent, R0=R0_low)
    green_min = Simulation(green_min_consts, TestPolicies.GREEN, people_per_simulation, is_stochastic=is_stochastic)
    green_max_consts = Consts(positive_tests_percent=max_percent, R0=R0_high)
    green_max = Simulation(green_max_consts, TestPolicies.GREEN, people_per_simulation, is_stochastic=is_stochastic)
    print_color_range("green", green_min, green_max)

    # yellow
    min_percent = 1
    max_percent = 5
    yellow_min_consts = Consts(positive_tests_percent=min_percent, R0=R0_low)
    yellow_min = Simulation(yellow_min_consts, TestPolicies.YELLOW, people_per_simulation, is_stochastic=is_stochastic)
    yellow_max_consts = Consts(positive_tests_percent=max_percent, R0=R0_high)
    yellow_max = Simulation(yellow_max_consts, TestPolicies.YELLOW, people_per_simulation, is_stochastic=is_stochastic)
    print_color_range("yellow", yellow_min, yellow_max)

    # orange
    min_percent = 5
    max_percent = 20
    orange_min_consts = Consts(positive_tests_percent=min_percent, R0=R0_low)
    orange_min = Simulation(orange_min_consts, TestPolicies.ORANGE, people_per_simulation, is_stochastic=is_stochastic)
    orange_max_consts = Consts(positive_tests_percent=max_percent, R0=R0_high)
    orange_max = Simulation(orange_max_consts, TestPolicies.ORANGE, people_per_simulation, is_stochastic=is_stochastic)
    print_color_range("orange", orange_min, orange_max)

    # red
    min_percent = 20
    max_percent = 60
    red_min_consts = Consts(positive_tests_percent=min_percent, R0=R0_low)
    red_min = Simulation(red_min_consts, TestPolicies.RED, people_per_simulation, is_stochastic=is_stochastic)
    red_max_consts = Consts(positive_tests_percent=max_percent, R0=R0_high)
    red_max = Simulation(red_max_consts, TestPolicies.RED, people_per_simulation, is_stochastic=is_stochastic)
    print_color_range("red", red_min, red_max)


def test_categories_affect(is_stochastic: bool = False):
    print("\nprinting protocols comparison:\n")
    people_per_simulation = 100_000
    consts = Consts(positive_tests_percent=2)
    print(consts)

    green = Simulation(consts, TestPolicies.GREEN, people_per_simulation, is_stochastic=is_stochastic)
    yellow = Simulation(consts, TestPolicies.YELLOW, people_per_simulation, is_stochastic=is_stochastic)
    orange = Simulation(consts, TestPolicies.ORANGE, people_per_simulation, is_stochastic=is_stochastic)
    red = Simulation(consts, TestPolicies.RED, people_per_simulation, is_stochastic=is_stochastic)

    print(f"green: {green.infected} \nyellow : {yellow.infected} \norange : {orange.infected} \nred : {red.infected}")


def optimize_one_test():
    class Policy:
        def __init__(self, tests):
            self.value = tests

    people_per_simulation = 100_000
    consts = Consts(positive_tests_percent=2.5)
    results = {}
    for day in range(1, consts.maximum_length_till_symptoms + 1):
        test_policy = Policy([day])
        simulation = Simulation(consts=consts, tests_policy=test_policy, people=people_per_simulation)
        results[day] = simulation.infected
    plt.plot(list(results.keys()), list(results.values()))
    plt.xlabel("day of test")
    plt.ylabel("total first circle infections")
    plt.title("optimize testing day")
    plt.show()


def optimize_two_tests():
    class Policy:
        def __init__(self, tests):
            self.value = tests

    people_per_simulation = 100_000
    consts = Consts(positive_tests_percent=5)
    days = consts.maximum_length_till_symptoms + 1
    # days = 7
    results = np.zeros(shape=(days + 1, days + 1))
    for day1 in range(1, days + 1):
        for day2 in range(1, days + 1):
            test_policy = Policy([day1, day2])
            simulation = Simulation(consts=consts, tests_policy=test_policy, people=people_per_simulation)
            results[day1, day2] = simulation.infected

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["green", "yellow", "red"])
    plt.pcolormesh(range(1, days+1), range(1, days+1), results[1:,1:], cmap=cmap)
    plt.colorbar()
    plt.xlabel("day of test 1")
    plt.ylabel("day of test 2")
    plt.title("expected number of first circle infections\ngiven the tests days")
    plt.show()

if __name__ == "__main__":
    # optimize_one_test()
    optimize_two_tests()
    # print_categories_boundaries(is_stochastic=False)
    # test_categories_affect()
