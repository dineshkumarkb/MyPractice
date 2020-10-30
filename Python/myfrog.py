def frog(x,y,d):

    distance = y-x

    if distance % d == 0:
        return distance//d
    else:
        return distance//d + 1


print(frog(10,85,30))