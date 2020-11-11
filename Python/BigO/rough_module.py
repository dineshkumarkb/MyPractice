"""
Calculate the sum of n numbers
"""

# def add_values(n):
#
#     summ = 0
#
#     for i in range(n):
#         summ += i
#
#     return summ
#
#
# print(add_values(1000))


def exception_testing():

    try:
        x = 10
        raise TypeError
        return x
    except Exception:
        pass
    finally:
        x = 40
        #return x


val = exception_testing()
print(val)
