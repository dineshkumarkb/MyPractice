""" Fibonacci Recursion
The mathematical formula for fibonacci is
fibonacci(n-1) + fibonacci(n-2)
Example : for calculating fibonacci of 5 numbers
we need to calculate fibonacci(4) + fibonacci(3)
"""

def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    return (fib(n-1) + fib(n-2))

print fib(9)