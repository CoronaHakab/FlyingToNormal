from src.consts import Consts
from src.tests_policy import TestPolicies
from src.simulation import Simulation


def test_total_infected_per_category():
    people_per_simulation = 100_000

    green_min_consts = Consts(P_per_milion_per_week=0, R0=1)
    green_min = Simulation(green_min_consts, TestPolicies.GREEN, people_per_simulation)
    green_max_consts = Consts(P_per_milion_per_week=1500, R0=3)
    green_max = Simulation(green_max_consts, TestPolicies.GREEN, people_per_simulation)

    yellow_min_consts = Consts(P_per_milion_per_week=1500, R0=1)
    yellow_min = Simulation(yellow_min_consts, TestPolicies.YELLOW, people_per_simulation)
    yellow_max_consts = Consts(P_per_milion_per_week=10000, R0=3)
    yellow_max = Simulation(yellow_max_consts, TestPolicies.YELLOW, people_per_simulation)

    orange_min_consts = Consts(P_per_milion_per_week=10000, R0=1)
    orange_min = Simulation(orange_min_consts, TestPolicies.ORANGE, people_per_simulation)
    orange_max_consts = Consts(P_per_milion_per_week=50000, R0=3)
    orange_max = Simulation(orange_max_consts, TestPolicies.ORANGE, people_per_simulation)

    red_min_consts = Consts(P_per_milion_per_week=50000, R0=1)
    red_min = Simulation(red_min_consts, TestPolicies.RED, people_per_simulation)
    red_max_consts = Consts(P_per_milion_per_week=200000, R0=3)
    red_max = Simulation(red_max_consts, TestPolicies.RED, people_per_simulation)

    print(
        f"green min: {green_min.infected} \nyellow min: {yellow_min.infected} \norange min: {orange_min.infected} \nred min: {red_min.infected}")
    print()
    print(
        f"green max: {green_max.infected} \nyellow max: {yellow_max.infected} \norange max: {orange_max.infected} \nred max: {red_max.infected}")


def test_categories_affect():
    people_per_simulation = 100_000
    consts = Consts(P_per_milion_per_week=2000)

    green = Simulation(consts, TestPolicies.GREEN, people_per_simulation)
    yellow = Simulation(consts, TestPolicies.YELLOW, people_per_simulation)
    orange = Simulation(consts, TestPolicies.ORANGE, people_per_simulation)
    red = Simulation(consts, TestPolicies.RED, people_per_simulation)

    print(f"green: {green.infected} \nyellow : {yellow.infected} \norange : {orange.infected} \nred :{red.infected}")


if __name__ == "__main__":
    test_total_infected_per_category()
    # test_categories_affect()

