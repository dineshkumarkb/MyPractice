








# Complete the secureChannel function below.
def secureChannel(operation, message, key):
    mylist = []
    mykey = list(map(int, key))
    print mykey
    if operation == 1:
            for i,j in zip(message,key):
                mylist.append(i*int(j))



            print "".join(mylist)







    elif operation == 2:
        for i in key:
            pass














if __name__ == '__main__':

    operation = int(raw_input().strip())

    message = raw_input()

    key = raw_input()

    res = secureChannel(operation, message, key)

