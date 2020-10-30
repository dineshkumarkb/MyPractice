def square_root(n):

    return n**0.5


#print square_root(28)


#Prime number square root logic
def is_prime(n):

    for i in range(2,n):
        if(i*i <= n):
            if(n%i == 0):
                return False
        return True


#print is_prime(4)


#Prime number normal logic
def check_prime(n):

    if(n==1):
        return "Number is one"

    for i in range(2,n-1):
        if(n%i == 0):
            return False
    return True


print check_prime(1)

