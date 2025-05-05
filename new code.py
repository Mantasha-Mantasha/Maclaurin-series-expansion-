import math

def maclaurin_series_expansion(func, x, n_terms):
    """
    Calculate the Maclaurin series expansion for a given function.

    Parameters:
        func (callable): The function to expand.
        x (float): The point at which to evaluate the expansion.
        n_terms (int): The number of terms in the expansion.

    Returns:
        float: The approximate value of the function at x using the Maclaurin series.
    """
    result = 0
    for n in range(n_terms):
        # Calculate the nth derivative at 0
        derivative = func(0, n)
        term = (derivative * (x**n)) / math.factorial(n)
        result += term
    return result

def example_function(x, n):
    """
    Example function to calculate the nth derivative of e^x at 0.
    (For e^x, all derivatives are e^x, and at x=0, the value is 1.)

    Parameters:
        x (float): The input value (ignored in this example).
        n (int): The order of the derivative.

    Returns:
        float: The value of the nth derivative at x=0.
    """
    return 1  # All derivatives of e^x are 1 at x=0

# Example usage
x_value = 1  # Point at which to evaluate the series (e.g., x=1)
n_terms = 5  # Number of terms in the series
result = maclaurin_series_expansion(example_function, x_value, n_terms)
print(f"Approximation of e^{x_value} using {n_terms} terms of Maclaurin series: {result}")
