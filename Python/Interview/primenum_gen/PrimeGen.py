class PrimeGen(object):

    def __init__(self,n):
        self.n = n


    def start_gen(self):
        for i in range(2,self.n):
            if(self._check_prime(i)):
                yield i

    def _check_prime(self,number):
         for i in range(2,number):
             try:
                 if(number % i ==  0):
                     return False
             except ZeroDivisionError:
                 pass
         return True




if __name__ == "__main__":
    p = PrimeGen(10)
    for j in p.start_gen():
        print j







