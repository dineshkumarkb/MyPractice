import time

def find_min_max(lst):
    max_val = 0
    min_val = 0
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    print(max_val, min_val)

find_min_max(lst=[23,1,45,5,22,90,12])
