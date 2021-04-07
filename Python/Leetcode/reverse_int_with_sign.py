def reverse_int(x: int) -> int:

    num_stack = list()

    if x == 0:
        return 0

    x = str(x)

    for i in range(len(x)-1, -1, -1):
        num_stack.append(x[i])

    if num_stack[-1] == "-":
        num_stack = num_stack[-1:] + num_stack[:len(num_stack)-1]

    reversed_final_val = int("".join(num_stack))

    if reversed_final_val >= pow(2,31) or reversed_final_val <= -2147483648:
        return 0

    return reversed_final_val


print(reverse_int(-123))
