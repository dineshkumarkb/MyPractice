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

#print(calc_sum(5))


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


def multi_part_add():
    tot_time_start = time.time()
    add1 = 0
    add2 = 0
    add1_start = time.time()
    for i in range(6):
        add1 += i
    add1_time = time.time() - add1_start

    # add2_start = time.time()
    # for j in range(10):
    #     add2 += j
    # add2_time = time.time() - add2_start

    tot_time = time.time() - tot_time_start

    print(f" Time taken for add1 : {add1_time}")
    #print(f" Time taken for add2 : {add2_time}")
    #print(f" Adding time: {add1_time + add2_time}")
    print(f" Total time : {tot_time} ")


multi_part_add()



