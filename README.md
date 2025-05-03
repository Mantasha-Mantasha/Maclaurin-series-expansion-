# Maclaurin-series-expansion-

import math
def maclaurin-series(f-derivatives,x, n-terms):
  """
  Calculate the Maclaurin series approximation for a funtion.

  Parameters:
     f-derivatives (list): List of derivatives of the function evaluated at 0.
     x (float): The point at which to approximatethe function.
     n-terms (init): Numbers of terms in the series.

  Returns:
     float: Approximation of the function at x.
  """
  approximation = 0
  for n in range(n-terms):
     term = (f-derivatives[n] * (x** n)) / math.factorial(n)
     approximation += term
  return approximation
