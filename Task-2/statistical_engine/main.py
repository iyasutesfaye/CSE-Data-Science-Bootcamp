from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

data = [50000, 52000, 51000, 700000, 48000, 49000, 1000000]

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Standard Deviation:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers(1.5))

print("\nMonte Carlo Simulation:")

days_list = [30, 365, 10000]

for days in days_list:
    result = simulate_crashes(days)
    print("Days:", days, "-> Probability:", result)