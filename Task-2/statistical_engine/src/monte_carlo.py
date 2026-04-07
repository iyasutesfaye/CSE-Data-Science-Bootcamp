import random

def simulate_crashes(days):
    crash_probability = 0.045
    crashes = 0

    for i in range(days):
        random_value = random.random()

        if random_value < crash_probability:
            crashes = crashes + 1

    return crashes / days