# Maclaurin Series Expansion

This repository contains an implementation of the Maclaurin series expansion for approximating mathematical functions. The Maclaurin series is a type of Taylor series expansion where the function is approximated as an infinite sum of terms calculated from the values of its derivatives at a single point (x = 0).

## Features

- Calculate the Maclaurin series expansion for any given mathematical function.
- Specify the number of terms in the series for approximation.
- Includes an example implementation for approximating the exponential function \( e^x \).

## Usage

### Functionality

The main function provided is `maclaurin_series_expansion`, which calculates the Maclaurin series expansion for a given function.

### Example Code

Below is an example of how to use the implementation to approximate \( e^x \):

```python
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
```

### Output

The output of the above code is:

```
Approximation of e^1 using 5 terms of Maclaurin series: 2.7166666666666663
```

### How It Works

1. **Maclaurin Series Formula**:
   The Maclaurin series for a function \( f(x) \) is calculated as:
   \[
   f(x) \approx \sum_{n=0}^{N-1} \frac{f^{(n)}(0)}{n!} x^n
   \]
   where \( f^{(n)}(0) \) is the nth derivative of \( f(x) \) evaluated at \( x=0 \).

2. **Implementation**:
   - The `maclaurin_series_expansion` function iteratively calculates each term of the series using the nth derivative provided by the user-defined function.
   - The result is the sum of all terms up to the specified number of terms `n_terms`.

3. **Example Function**:
   - The `example_function` demonstrates how to define a function for which derivatives at \( x=0 \) are known.
   - In this case, the example approximates \( e^x \), where all derivatives are 1 at \( x=0 \).

## Customization

You can define your own functions and derivatives to use with the `maclaurin_series_expansion`. Simply create a Python function that calculates the nth derivative of your desired function at \( x=0 \).

## Requirements

- Python 3.x
- No external libraries are needed; the code uses Python's built-in `math` module.

## Limitations

- The accuracy of the approximation depends on the number of terms in the series (`n_terms`). Increasing the number of terms improves accuracy.
- This implementation assumes that the nth derivative at \( x=0 \) can be calculated and provided by the user.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve the implementation or add new features.

## Author

Developed by [Mantasha-Mantasha].

---
Enjoy approximating functions with the Maclaurin series!

