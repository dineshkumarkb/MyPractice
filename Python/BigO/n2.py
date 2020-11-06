"""
This program demonstrates the O(n2) time complexity
For every element in the outer for loop, the inner for loop executes n times,
where n is the length of the inner loop

"""
import time


def print_cord():

    a = range(100)
    b = range(100)

    start = time.time()
    for i in a:
        for j in b:
            print(i, j)
    end = time.time()
    total_time = end - start
    print(f" The total time is: {total_time} ")


print_cord()