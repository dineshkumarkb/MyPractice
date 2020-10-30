def calc_fib(n):
    l = []
    for i in range(n):
        l.append(0)

    for i in range(n):
        fib_gen(i,l)
    print l

def fib_gen(n,l):
    if n == 0:
        return 0
    elif n==1:
        return 1
    elif l[n] > 0:
        return l[n]
    l[n] = fib_gen(n-1,l) + fib_gen(n-2,l)


#calc_fib(10)



def gen_prime(n):
    l = []
    for i in range(n):
        l.append(0)

    for i in range(n):
        prime_gen(i,l)

    print l


def prime_gen(n,l):

    if n==0:
        return 0
    elif n==1:
        return 1
    elif l[n] > 0:
        return l[n]
    if(check_prime(n)):
        l[n] = n
    prime_gen(n-1,l)




def check_prime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True




gen_prime(10)