"""
This program calculates the fibonacci series using recursion
The time complexity is O(2^n)
"""

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#print(fib(6))


def fib_non_rec(n):
    if n == 1:
        return n
    a = 0
    b = 1
    fib = 0

    for i in range(1,n):
        fib = a + b
        a,b = b, fib
        print(fib)


fib_non_rec(10)
