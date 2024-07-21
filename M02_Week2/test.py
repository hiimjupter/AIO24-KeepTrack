import numpy as np


def compute_eigenvalues_eigenvectors_manual(M):
    # Step 1: Characteristic Polynomial
    a, b = M[0, 0], M[0, 1]
    c, d = M[1, 0], M[1, 1]

    # Step 2: Solving for Eigenvalues
    coefficients = [1, -(a + d), a*d - b*c]
    eigenvalues = np.roots(coefficients)

    # Step 3: Finding Eigenvectors
    eigenvectors = []
    for eigenvalue in eigenvalues:
        A = M - eigenvalue * np.eye(2)
        _, _, vh = np.linalg.svd(A)
        eigenvector = vh[-1]
        # Normalize eigenvector
        eigenvectors.append(eigenvector / eigenvector[0])

    # Convert list of eigenvectors to numpy array
    eigenvectors = np.array(eigenvectors).T

    return eigenvalues, eigenvectors


# Example matrix
M = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors_manual(M)

eigenvalues, eigenvectors
