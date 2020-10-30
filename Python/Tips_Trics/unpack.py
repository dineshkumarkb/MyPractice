def myunpack1(*args):
    print(" The args are ", args)

def myunpack2(**kwargs):
    print(" The kwargs are ", kwargs)


def myunpack3(num1,num2):
    print(" The value is {}".format(num1+num2))




if __name__ == "__main__":
    test_data = [1,2]
    myunpack1(1,2,3)
    myunpack2(val1=4,val2=5,val3=6,val4=7)
    print(" The unpacked value is ", *test_data)
    myunpack3(*test_data)