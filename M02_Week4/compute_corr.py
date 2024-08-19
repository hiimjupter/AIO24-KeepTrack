import numpy as np


def compute_correlation(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0

    multiply_array = np.multiply(X, Y)

    numerator = (N*np.sum(multiply_array)) - (np.sum(X) * np.sum(Y))

    std_X = np.sqrt(N*np.sum(np.power(X, 2)) - np.power(np.sum(X), 2))
    std_Y = np.sqrt(N*np.sum(np.power(Y, 2)) - np.power(np.sum(Y), 2))

    denominator = std_X * std_Y

    return round((numerator/denominator), 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])

computed_corr = compute_correlation(X, Y)
expected_corr = 0.42

assert np.isclose(
    computed_corr, expected_corr), f"Result should be {expected_corr}"
print("Test passed")
