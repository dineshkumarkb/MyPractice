
def findDamagedToy(N, T, D):
    #Write your code here
    count = 0
    # for i in range(D,N):
    #     count+=1
    #     if(count == T):
    #         print i

    mylist = range(1,N+1)
    mylist = mylist[D-1:] + mylist[:D-1]
    print mylist
    while(T != 0):
        for i in mylist:
            T-=1
            if(T==0):
                print i
                break











if __name__ == '__main__':

    N = int(raw_input().strip())

    T = int(raw_input().strip())

    D = int(raw_input().strip())

    result = findDamagedToy(N, T, D)

