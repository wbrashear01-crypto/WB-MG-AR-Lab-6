def sum_of_odds(n):
  """
  positive integer -> integer
This function returns the sum of all the odd numbers less than than or equal to n.
  >>> sum_of_odds(3):
  4
  >>> sum_of_odds(4):
  4
  >>> sum_of_odds(0):
  0
  """
total=0
k=1
while k<=n:
  total=total+k
  k=k+2
return total
