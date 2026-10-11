def combine_sequence(n,f=None ,combine=None): #modify this line as needed to meet the prompt with as minimal change as possible
  """
  number->number
  takes in a postive number n and two functions and combines a line of numbers from 1 to n. If f and combine are not given values then the numbers are summed from 1 to n.
  >>> combine_sequence(5, identity, add)
  15
  >>> combine_sequence(3, identity, add)
  6
  """
  if f is None: f= identify
  if combine is None: combine=add

def add(x,y):
   return x + y
def identity(x):
   return x
  if n==1:
    return f(1)
  else:
    return combine(combine_sequence(n-1, f, combine), f(n))
