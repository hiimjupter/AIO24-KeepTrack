import numpy as np


def compute_mean(X):
    mean = np.sum(X)/len(X)  # or np.mean(X)
    return mean


def compute_std(X):
    mean = compute_mean(X)
    variance = 0

    subtract_array = np.subtract(X, mean)
    power_array = np.power(subtract_array, 2)
    variance = np.mean(power_array)

    return round(np.sqrt(variance), 2)


# Test case
X = [171, 176, 155, 167, 169, 182]
expected_std = 8.33

# Compute the mean using the function
computed_std = compute_std(X)

# Assert to check if the computed mean matches the expected mean
assert np.isclose(
    computed_std, expected_std), f"Result should be {expected_std}"

print("Test passed!")
