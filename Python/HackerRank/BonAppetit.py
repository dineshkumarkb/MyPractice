def check_appt(k,arr,amt):
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]


    act_bill = (tot - (arr[int(k)]))//2
    if(act_bill == amt):
        print "Bon Appetit"
    else:
        print abs(act_bill - amt)


if __name__ == "__main__":
    n,k = raw_input().split()
    arr  = map(int,raw_input().split())
    amt = input()
    check_appt(k,arr,amt)