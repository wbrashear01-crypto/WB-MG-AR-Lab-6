def nth_powers(n,m):
"""
positive integer, positive integer -> positive integers
This function takes in two posititve integer m and n and prints 1^n 2^n 3^n....m^n.
>>> nth_powers(2,3)
1 4 9
>>> nth_powers(3,4)
1 8 27 256
>>> nth_powers(2,2)
1 4
"""
if m==1:
  print(1**n)
else:
  nth_powers(n,m-1)
  print(m**n)
