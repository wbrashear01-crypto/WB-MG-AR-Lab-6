def sum_squares(n):
  """
  number -> number
  takes in a positive number n and returns the sum of the square of the numbers from 1 to n: 1^2+2^2+3^2+...+n^2.
  >>> sum_squares(3)
  14
  >>> sum_squares(5)
  55
  """
  if n==1:
    return 1
  else:
    return (n ** 2) + sum_squares(n-1)
