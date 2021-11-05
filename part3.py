"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""

def isprime(number):
 for i in range(2, number//2+1):
   #for 4 as a specific case with the end range, number//2 does not work 
   #inside range should be integer; starts at 0 if not specified
   if number % i == 0: 
     return False
    #else means that loop will only run once --> just put return true
   return True

