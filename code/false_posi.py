def false_position(f, a, b, tol=1e-5, max_iter=1000):
    """
    Solves the equation f(x) = 0 using the False Position (Regula Falsi) method.
    
    Args:
    f: A callable function for which the root is to be found.
    a, b: Floats, the initial bracketing interval [a, b].
    tol: Tolerance for the solution (default 1e-5).
    max_iter: Maximum number of iterations allowed (default 1000).
    
    Returns:
    The estimated root of the function.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Function does not change sign over the initial interval. Please provide a different interval.")
    
    for i in range(max_iter):
        # Compute the point 'c' where the line through (a, f(a)) and (b, f(b)) crosses the x-axis
        fa = f(a)
        fb = f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)

        # Check if the accuracy goal has been met
        if abs(fc) < tol:
            return c

        # Determine the new interval [a, b]
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc

        # If c is very close to a or b, we might need additional precision checks
        if abs(b - a) < tol:
            return c

    raise RuntimeError(f"No convergence after {max_iter} iterations.")

# Example function: x^2 - 4
def example_function(x):
    return x**2 - 4

# Find the root
root = false_position(example_function, 1, 3)
print("Root:", root)

