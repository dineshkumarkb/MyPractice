def shift_array_right(arr):
    print "Starting right shift"
    j = 1
    while(j < len(arr)):
        print arr[j:] + arr[:j]
        j+=1

def shift_array_left(arr):
    print "Starting left shift"
    j = 1
    while (j < len(arr)):
        print arr[-j:] + arr[:-j]
        j += 1





#shift_array_right(range(1,10))
shift_array_left(range(1,10))
