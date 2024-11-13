def modified_secant(f, x0, delta=1e-4, tol=1e-5, max_iter=1000):
    """
    Finds the root of a function using the Modified Secant Method.
    
    Args:
    f: A callable function for which the root is to be found.
    x0: The initial guess for the root.
    delta: The perturbation factor (default is 1e-4).
    tol: The tolerance for stopping the algorithm (default is 1e-5).
    max_iter: The maximum number of iterations (default is 1000).
    
    Returns:
    The estimated root of the function.
    """
    for _ in range(max_iter):
        # Calculate the approximate derivative
        f_prime = (f(x0 + delta * x0) - f(x0)) / (delta * x0)
        
        # If the derivative is very small, halt to avoid division by near zero
        if abs(f_prime) < tol:
            raise ValueError("Derivative too small. No solution found.")
        
        # Calculate the next approximation
        x1 = x0 - f(x0) / f_prime
        
        # Check for convergence
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1
    
    raise RuntimeError(f"No convergence after {max_iter} iterations.")

# Example usage:
def example_function(x):
    return x**2 - 4

initial_guess = 2.5
root = modified_secant(example_function, initial_guess)
print("Root:", root)

