class SlidingWindow(object):

    def __init__(self,width=0):

        if(width != 0):
            self.win_width = width
        else:
            raise Exception ("Non zero width or size")


    def slide_window(self,arr):

        for i in range(1,len(arr)):
            print arr[i:self.win_width+i]



if __name__ == "__main__":
    a =  range(20)
    s = SlidingWindow(5)
    s.slide_window(a)