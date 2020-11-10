import time

"""
Return the sum of given n numbers using recursion
"""


def calc_sum(n):
    """
    This function calculates the sum using time complexity : O(n) and space complexity O(n).
    At any given point of time the stack size is equal to n as we use recursion
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    else:
        print(f" Calculating {n} + calc_sum({n-1})")
        return n + calc_sum(n-1)

print(calc_sum(5))


def calc_sum_wo_recursion(n):
    """
    Here the time complexity is O(n) and the space complexity is O(1) unlike the previous one
    :param n:
    :return:
    """

    add = 0
    for i in range(n+1):
        print(f" Adding {i} ")
        add += add_num(i)
    return add


def add_num(a):
    return a


#print(calc_sum_wo_recursion(5))

"""
Multi part algorithms -- add
"""


# def multi_part_add(a,b):
#
#     add1 = 0
#     add2 = 0
#
#     # sum all the elements in a
#     for i in range(a):
#         add1 += i
#
#     # sum all the elements in b
#     for j in range(b):
#         add2 += j
#
#     print(add1,add2)
#
#
# multi_part_add(5,10)



