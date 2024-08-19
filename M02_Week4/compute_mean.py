import numpy as np


def compute_mean(X):
    mean = np.sum(X)/len(X)  # or np.mean(X)
    return mean


# Test case
X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
expected_mean = 1.8

# Compute the mean using the function
computed_mean = compute_mean(X)

# Assert to check if the computed mean matches the expected mean
assert np.isclose(
    computed_mean, expected_mean), f"Result should be {expected_mean}"

print("Test passed!")
