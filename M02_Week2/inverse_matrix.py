import numpy as np


def inverse_matrix(matrix):
    # Only apply for square matrix 2x2
    deter = np.linalg.det(matrix)
    if deter == 0:
        return "Matrix is singular and cannot be inverted."

    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
    result = (1 / deter) * np.array([[d, -b], [-c, a]])

    return result


m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)
