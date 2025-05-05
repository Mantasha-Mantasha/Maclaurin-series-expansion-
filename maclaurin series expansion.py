import math

def maclaurin_series(func, n_terms, x_val):
    """
    Compute the Maclaurin series expansion for a given function.

    Parameters:
    func (function): The function to expand (e.g., math.sin, math.exp).
    n_terms (int): The number of terms in the series expansion.
    x_val (float): The value of x at which to evaluate the series.

    Returns:
    float: The approximate value of the function at x using the Maclaurin series.
    """
    # Compute the series expansion
    result = 0
    for n in range(n_terms):
        # Compute the nth derivative at x=0
        derivative_at_zero = func(0, n)
        
        # Compute the nth term of the series
        term = (derivative_at_zero / math.factorial(n)) * (x_val ** n)
        result += term
    
    return result

# Example function: sin(x)
def sin_derivative(x, n):
    """
    Compute the nth derivative of sin(x) at x=0.
    
    Parameters:
    x (float): The value of x (not relevant for this implementation).
    n (int): The derivative order.

    Returns:
    float: The value of the nth derivative at x=0.
    """
    # The derivatives cycle: sin, cos, -sin, -cos
    derivatives = [0, 1, 0,-1,]
    
``
It seems my response was cut off. Here is the full implementation of a Maclaurin series for specific functions like \( \sin(x) \) and \( \cos(x) \). You can also generalize it further.

```python name=maclaurin_series.py
import math

def maclaurin_series(func_derivative, n_terms, x_val):
    """
    Compute the Maclaurin series expansion for a given function.

    Parameters:
    func_derivative (function): A function that returns the nth derivative at x=0.
    n_terms (int): The number of terms in the series expansion.
    x_val (float): The value of x at which to evaluate the series.

    Returns:
    float: The approximate value of the function at x using the Maclaurin series.
    """
    # Compute the series expansion
    result = 0
    for n in range(n_terms):
        # Compute the nth derivative at x=0
        derivative_at_zero = func_derivative(n)
        
        # Compute the nth term of the series
        term = (derivative_at_zero / math.factorial(n)) * (x_val ** n)
        result += term
    
    return result

# Example function: sin(x)
def sin_derivative(n):
    """
    Compute the nth derivative of sin(x) at x=0.
    
    Parameters:
    n (int): The derivative order.

    Returns:
    float: The value of the nth derivative at x=0.
    """
    # The derivatives cycle: sin -> cos -> -sin -> -cos
    cycle = [0, 1, 0, -1]  # sin(0), cos(0), -sin(0), -cos(0)
    return cycle[n % 4]

# Example function: cos(x)
def cos_derivative(n):
    """
    Compute the nth derivative of cos(x) at x=0.
    
    Parameters:
    n (int): The derivative order.

    Returns:
    float: The value of the nth derivative at x=0.
    """
    # The derivatives cycle: cos -> -sin -> -cos -> sin
    cycle = [1, 0, -1, 0]  # cos(0), -sin(0), -cos(0), sin(0)
    return cycle[n % 4]

# Usage examples
x_value = math.pi / 4  # Example value of x (π/4)
terms = 10            # Number of terms in the series

# Approximation for sin(x)
sin_approx = maclaurin_series(sin_derivative, terms, x_value)
print(f"Maclaurin series approximation for sin({x_value}): {sin_approx}")
print(f"Exact value of sin({x_value}): {math.sin(x_value)}")

# Approximation for cos(x)
cos_approx = maclaurin_series(cos_derivative, terms, x_value)
print(f"Maclaurin series approximation for cos({x_value}): {cos_approx}")
print(f"Exact value of cos({x_value}): {math.cos(x_value)}")
