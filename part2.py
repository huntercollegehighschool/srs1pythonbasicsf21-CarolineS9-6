"""
Define a function twodigitodd that take a single integer argument (number). The function should return True if the number is a two digit odd number, and False if it is not.
"""

def twodigitodd(number):
  if number % 2 != 0 and number > 9 and number < 100:
    return(True)
  else:
      return(False)

