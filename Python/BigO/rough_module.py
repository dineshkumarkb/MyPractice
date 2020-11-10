"""
Calculate the sum of n numbers
"""

def add_values(n):

    summ = 0

    for i in range(n):
        summ += i

    return summ


print(add_values(1000))
