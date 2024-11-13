from typing import Callable

def bisection_method(f: Callable[[float], float], a: float, b: float, tol: float = 1e-5, max_iter: int = 1000) -> float:
    if f(a) * f(b) >= 0:
        raise ValueError("Function does not change sign over the initial interval. Please provide a different interval.")
    
    c = (a + b) / 2.0
    fc = f(c)
    count = 0
    
    while abs(fc) > tol and count < max_iter:
        count += 1
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        c = (a + b) / 2.0
        fc = f(c)
    
    if count >= max_iter:
        print("Maximum number of iterations reached.")
    
    return c

# Example function with type hint
def example_function(x: float) -> float:
    return x**2 - 4

# Example usage
root = bisection_method(example_function, 1, 3)
print("Root:", root)

