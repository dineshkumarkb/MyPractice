cube = lambda x:x**3
l = [0,1]
def fibonacci(n):
    if(n == 0):
        return []
    elif(n == 1):
        return [1]
    for i in range(2,n):
        l.append(l[-2] + l[-1])
    return l




if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))