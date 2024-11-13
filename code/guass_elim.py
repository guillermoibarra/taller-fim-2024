import numpy as np

def gaussian_elimination(a, b):
    """
    Solves the system of linear equations Ax = b using naive Gaussian elimination.
    
    :param a: Coefficient matrix (2D numpy array)
    :param b: Right-hand side vector (1D numpy array)
    :return: Solution vector (1D numpy array)
    """
    n = len(b)
    A = np.hstack((a, b.reshape(-1, 1)))  # Create the augmented matrix

    # Forward elimination
    for i in range(n):
        # Make the i-th row pivot 1 and eliminate all values below it
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, i + 1:n], x[i + 1:n])) / A[i, i]

    return x

# Example of use:
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

solution = gaussian_elimination(A, b)
print("Solution:", solution)

