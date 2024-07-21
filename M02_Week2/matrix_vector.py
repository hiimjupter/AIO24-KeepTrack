import numpy as np


def matrix_multi_vector(matrix, vector):
    reshape_vector = vector[:, np.newaxis].T  # reshape
    mat_mul_vect = matrix * reshape_vector
    result = np.sum(mat_mul_vect, axis=1)  # sum of columns -> each result

    return result  # np.dot(matrix, vector)


m = np.array([[-1, 1, 1],
              [0, -4, 9]])
v = np.array([0, 2, 1])

result = matrix_multi_vector(m, v)
print(result)
