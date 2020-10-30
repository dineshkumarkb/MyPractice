# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")

def solution(N):
    # write your code in Python 3.6

    for i in range(1, N+1):
        rep_str = ""
        is_div = False
        if i % 2 == 0:
            is_div = True
            rep_str += "Codility"
        if i % 3 == 0:
            is_div = True
            rep_str += "Test"
        if i % 5 == 0:
            is_div = True
            rep_str += "Coders"
        if is_div:
            print(rep_str)
        else:
            print(i)


