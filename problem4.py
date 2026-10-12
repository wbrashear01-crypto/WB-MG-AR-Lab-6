def factorial_trailing_zeros(n):
  """
  integer -> integer

  It asks how many whole times 5 fit into n. This helps count the factors of 5  in n!, which determines the number of trailing zeros.

  >>> factorial_trailing_zeros(4)
  0
  >>> factorial_trailing_zeros(5)
  1
  >>> factorial_trailing_zeros(17)
  3
  """
  
  return n // 5
