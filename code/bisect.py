def bisection_method(f, a, b, tol=1e-5, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("Function does not change sign over the initial interval. Please provide a different interval.")
    
    # Initial midpoint and function evaluation at midpoint
    c = (a + b) / 2.0
    fc = f(c)
    
    # Counter for iterations
    count = 0
    
    while abs(fc) > tol and count < max_iter:
        # Update the counter
        count += 1
        
        # Check which subinterval to choose based on where the sign change occurs
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        # Calculate new midpoint and function value
        c = (a + b) / 2.0
        fc = f(c)
    
    if count >= max_iter:
        print("Maximum number of iterations reached.")
    
    return c

# Example function: x^2 - 4 (whose roots are x = -2, 2)
def example_function(x):
    return x**2 - 4

# Finding the root near 1
root = bisection_method(example_function, 1, 3, tol=1e-10, max_iter=2000)
print("Root:", root)

