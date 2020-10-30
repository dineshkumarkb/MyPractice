def myintegers(count_int):
    for i in range(count_int):
        yield i


def square_me(num_seq):
    for j in num_seq:
        yield j*j


print(list(square_me(myintegers(10))))


# Above code represented as generator expressions

mynumbers = range(10)
ret_num = (i for i in mynumbers)
square_num = (j*j for j in ret_num)
print(list(square_num))
