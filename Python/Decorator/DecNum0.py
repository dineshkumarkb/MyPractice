
def test_neg(func):

    def inner(*args):

        print " the args are ",args

        n = args[1]
        mtd = args[0]

        if(n <= 1):
            print " Number is one so it is neither prime nor comp "
            return
        else:
            return func(mtd,n)

    return inner




class FindPrime(object):

    def __init__(self,n):
        self.n = n
        self.calc_prime(self.n)


    @test_neg
    def calc_prime(self,p_num):

        for i in range(2,p_num):
            if(p_num % i == 0):
                print " Number is not prime "
                break
            else:
                print "Prime number"


f = FindPrime(1)




