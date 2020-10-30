def slide_window(arr,width):
    for i in range(len(arr)):
        print arr[i:width+i]


def slide_me(arr,width):
    j = 0
    while(j < len(arr)):
        print arr[j:width+j]
        j+=1


#slide_window(range(1,10),5)
slide_me(range(1,10),3)
