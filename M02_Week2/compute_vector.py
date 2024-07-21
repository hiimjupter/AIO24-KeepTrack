import numpy as np


def compute_vector_length(vector):
    # Method 1
    sq_vector = np.square(vector)  # = vector*vector
    sum_sq_vector = np.sum(sq_vector)
    len_of_vector = np.sqrt(sum_sq_vector)

    return len_of_vector  # or Method 2: using np.linalg.norm(vector)


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))
