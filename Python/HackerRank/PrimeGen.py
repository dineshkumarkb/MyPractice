class PrimeGen(object):

    def __init__(self):
        pass

    def check_prime(self,n):

        for i in range(2,n):
            if(n != i and n % i == 0):
                return False

        return True

    def gen_prime(self,n):
        for i in range(n):
            if(self.check_prime(i)):
                print i



if __name__ == "__main__":
    p = PrimeGen()
    print p.check_prime(2)
    p.gen_prime(20)


