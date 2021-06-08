# def fib(n):

#     if n == 0:
#         return

#     count = 0
#     a = 0
#     b = 1
#     while count <= n:
#         c = a + b
#         a,b = b,c
#         count += 1

#     yield c


# # fib_value_10 = fib(10)
# # print(fib_value)
# # print(next(fib_value))
# # fib_value(20)


# # def fib(n):

# #     lst = [0,1]

# #     for i in range(n):
# #         lst.append(lst[-1] + lst[-2])

# #     print(lst)


# # fib(11)


# def ret_num(n):

#     lst = range(n)
#     print(lst)

#     for i in lst:
#         yield i

# ret_val = ret_num(5)
# print(next(ret_val))
# print(next(ret_val))
# print(next(ret_val))

# class RetNum():

#     def __init__(self):
#         super().__init__()

#     def __iter__(self, count):
#         self.count = 0

#     def __next__():

#         if condition:
#             raise StopIteration
#         else:
#             ...

a = [1, 2, 3]


def f(b):
    b[2][1] = 14

    print(b)



# a[1] = 12

# print(a) #=> [1,12,3]
# f(a) #=> [1,12,13]

# a = (1, 3, [12,13], 14)
# f(a) # => (1,3, 13, 14)


# class Calc:

#     @swap_values
#     def difference(a, b):

#         return a - b


# def swap_values(a, b):

#     def actual_swap():
#         if b > a:
#             a, b= b,a
#         return actual_swap

#     return swap_values


#     a = [1,1,1,1]


#     3 => 1,1,1
#        1, 3
#        2 , 3

#        max = 2

# a = [1,1,1]
# 1, 3, 4

# 1,2,3
# 2,3
# 1,3


# 1,3   => Skipping 2         2,3,4
#                             2,4

# 1,2,3,4  =
# 1,2,4
# 1,2,3

matix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1,2,3,6,9,8,7,4,5
# [0][0] [0][1] [0][2] [1][2] [2][2] [2][1] [2][0] [1][0] [1][1]

for i in range(len(matix[0])):
    # print(f"Matix[i]:{matix[i]}")
    for j in range(len(matix[i])):
        if i == 0:
            print(matix[i][j], end=" ")
        elif i == 1:
            print(matix[i][-j], end=" ")

# m = [
#     [1,2],
#     [3,4]
# ]

# => 1,2,4,3
# [0][0] [0][1] [1][1] [1][0]
# for i in range(len(m)):
#     for j in range(len)

