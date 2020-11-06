"""
This program illustrates how to square a number using recursion
"""


def get_square(n):
    print(f" The n value is {n}")
    if n == 1:
        return 1
    else:
        prev = get_square(n-1)
        #print(f" The prev: {prev}")
        curr = prev * prev
        print(curr)
        return n

get_square(50)