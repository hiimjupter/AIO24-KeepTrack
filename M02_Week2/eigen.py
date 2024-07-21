import numpy as np


def compute_eigenvalues_eigenvectors(M):
    eigenvalues, eigenvectors = np.linalg.eig(M)

    return eigenvalues, eigenvectors


matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvalues, '\n', eigenvectors)
