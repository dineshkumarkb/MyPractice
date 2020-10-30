from myexcept import subnum, mulnum


class TestSub(object):

    def testsub(self):
        x = 10
        y = 5
        result = x - y
        assert result == subnum(x, y)


    def testsubneg(self):
        x = -10
        y = 5
        result = x - y
        assert result == subnum(x, y)


    def testsublarge(self):
        x = 1000000000000000
        y = 58623738468736
        result = x - y
        assert result == subnum(x, y)



class TestMul(object):

    def testmul(self):
        x = 10
        y = 5
        result = x * y
        assert result == mulnum(x, y)



    def testmulneg(self):
        x = -10
        y = 5
        result = x * y
        assert result == mulnum(x, y)


    def testmullarge(self):
        x = 1000000000000000
        y = 58623738468736
        result = x * y
        assert result == mulnum(x, y)
