def mult_funct(n,f):
'''
positive integer, function -> integer
This function returns the product of f(1)*f(2)*...*f(n).
>>> mult_funct(3, the_same)
6
>>> mult_funct(3, square)
36
>>> mult_funct(3, double)
48
'''
total=1
k=1
while k<=n:
  total=total*f(k)
  k=k+1
return total

def the_same(x):
  return x
def square(x):
  return x*x
def double(x):
  return 2*x
