from src.consts import Consts
from src.tests_policy import TestPolicies
from src.simulation import Simulation
import matplotlib.pyplot as plt


def print_categories_boundaries(people_per_simulation: int = 100_000, R0_low: float = 1.0, R0_high: float = 2.0,
                                is_stochastic: bool = False):
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


def test_categories_affect():
    people_per_simulation = 100_000
    consts = Consts(P_per_milion_per_week=2000)

    green = Simulation(consts, TestPolicies.GREEN, people_per_simulation)
    yellow = Simulation(consts, TestPolicies.YELLOW, people_per_simulation)
    orange = Simulation(consts, TestPolicies.ORANGE, people_per_simulation)
    red = Simulation(consts, TestPolicies.RED, people_per_simulation)

    print(f"green: {green} \nyellow : {yellow} \norange : {orange} \nred :{red}")


if __name__ == "__main__":
    print_categories_boundaries()
    # test_categories_affect()
