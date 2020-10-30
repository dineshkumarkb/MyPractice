# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter
import time

# def solution(N):
#     # write your code in Python 3.6
#     decimal_rep = 11**N
#     #print(f" The decimal rep is {decimal_rep} ")
#     count = 0
#     for i in str(decimal_rep):
#         if i == "1":
#             count += 1
#
#     return count


def solution(N):
    # write your code in Python 3.6
    decimal_rep = 11**N
    count = dict()
    #print(f" The decimal rep is {decimal_rep} ")
    for i in str(decimal_rep):
        keys = count.keys()
        if str(i) in keys:
            count[str(i)] += 1
        else:
            count[str(i)] = 1

    return count.get("1", 0)

time_before = time.time()
print(solution(999))
time_after = time.time()
exec_time = time_after - time_before
print(exec_time)

