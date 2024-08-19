import numpy as np


def compute_median(X):
    size = len(X)
    X = np.sort(X)

    if size % 2 != 0:
        middle_index = (size + 1)/2
        median = X[middle_index]
    else:
        first_middle_index = int(size/2) - 1
        second_middle_index = int((size/2) + 1) - 1
        median = (X[first_middle_index] + X[second_middle_index])/2
    # median = np.median(X)

    return median


# Test case
X = [1, 5, 4, 4, 9, 13]
expected_median = 4.5

# Compute the mean using the function
computed_median = compute_median(X)

# Assert to check if the computed mean matches the expected mean
assert np.isclose(
    computed_median, expected_median), f"Result should be {expected_median}"

print("Test passed!")
