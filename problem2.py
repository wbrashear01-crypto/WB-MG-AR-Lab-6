def powers_of_two(n):
  """
  number -> number
  take as imput a positive integer n and will print all of the powers of two that are less than or equal to n
  >>> powers_of_two(2)
  2
  >>> powers_of_two(8)
  2
  4
  8
  """
  if n==1:
    return 0
  elif  2**1<=n:
    m=1
    m=1+m
    print(2**1)
  if 2**m<=n:
    m=1+m
    print(2**m)
    powers_of_two(n)
    print(2**)
  else:
    m=1+m
    powers_of_two(n-1)
    print(2
    
  
    
    
