def newton_raphson(f, df, x0, tol=1e-5, max_iter=1000):
    """
    Solves the equation f(x) = 0 using the Newton-Raphson method.
    
    Args:
    f: A callable function for which the root is to be found.
    df: The derivative of the function f.
    x0: Initial guess for the root.
    tol: Tolerance for the solution (default 1e-5).
    max_iter: Maximum number of iterations allowed (default 1000).
    
    Returns:
    The estimated root of the function.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        
        # Calculate the next guess for the root
        x_new = x - fx / dfx
        
        # Check for convergence
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    raise RuntimeError(f"No convergence after {max_iter} iterations.")

def f(x):
    return x**2 - 4

def df(x):
    return 2*x

initial_guess = 1.0
root = newton_raphson(f, df, initial_guess)
print("Root:", root)

