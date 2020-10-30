import pandas
import numpy



l = [1,2,3,4,5]

def print_func(myobj):

    if isinstance(l,(list,)):
        print(" The elements of the list are ",l)
    else:
        print(" The object is not a list ")


print_func(l)