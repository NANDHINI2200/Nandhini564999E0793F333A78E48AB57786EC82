def factorial(n):
  return 1 if (n==1 or n==0)  else n * factorial(n-1);
 
#Enter input
n = int(input("Enter input number : "))
 
print("The factorial of",n,"is",factorial(n))