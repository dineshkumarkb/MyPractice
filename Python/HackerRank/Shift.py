def left_shift(n,a):
    if hasattr(a,"append"):
        print a[n:]+a[:n]
    else:
        raise Exception,"a is not a list"


def right_shift(n,a):
    if hasattr(a,"append"):
        print a[-n:]+a[:-n]
    else:
        raise Exception,"a is not a list"

a = [1,2,3,4,5]
left_shift(2,a)
right_shift(2,a)
