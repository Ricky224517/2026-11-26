import D1546985_math as x1
import cli_draw as x2

n = int(input("n="))
if x1.isPrime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")  
    
x2.fun1(3, "*")     