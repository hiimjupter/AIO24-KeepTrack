import numpy as np


def compute_cosine(x, y):
    dot_product = x.dot(y)
    mul_vectors_len = np.linalg.norm(x)*np.linalg.norm(y)
    result = dot_product/mul_vectors_len

    return result


x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
