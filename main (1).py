# Implement a recursive function to calculate the factorial of a given a number 

def fact_rec(n):
  if n==0 or n==0:
       return 1
  else:
   return n*fact_rec(n-1)

number=2
res = fact_rec(number)

print("The factorial of {} is{}". format(number,res))
