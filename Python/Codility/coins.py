# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    reverse_count = 0

    if len(A) == 1:
        return 0

    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            reverse_count += 1

    return reverse_count


if __name__ == "__main__":
    a = [0, 1, 1, 0]
    print(solution(a))
