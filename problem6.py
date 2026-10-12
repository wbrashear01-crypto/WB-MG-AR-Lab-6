def sum_funct(n,f):
  """
  integer -> integer
  Returns the sum of f(1) + f(2) + ... + f(n).

  >>> sum_funct(4, square)
  30
  >>> sum_funct(4, double)
  20
  """
  total = 0
  i = 1
  while i <= n:
      total = total + f(i)
      i = i + 1
  return total

def square(x):
  return x*x

def double(x):
  return 2*x

