"""
This is a program for a binary search of an element.
In every iteration, the search list is halved.

For example in the below program
Iteration 1 : The list is [2,3,4,5,6,7,8,9,10,11]
Iteration 2 : [7, 8, 9, 10, 11]
Iteration 3 : [9, 10, 11]
Iteration 4 : [10, 11]


"""

def search(n, lst):

    print(f" The list is {lst} ")

    pivot = len(lst)//2

    print(f" Pivot element : {pivot}")

    if n == lst[pivot]:
        print(f" n is pivot : {pivot}")
        return "Element found"
    elif n < lst[pivot]:
        print(f" n : {n} is less than pivot : {pivot}")
        lst = lst[:pivot]
        print(f" The shrinked list: {lst}")
        return search(n, lst)
    elif n > lst[pivot]:
        print(f" n : {n} is greater than pivot : {pivot}")
        lst = lst[pivot:]
        print(f" The shrinked list: {lst}")
        return search(n, lst)


print(search(7, lst = [2,3,4,5,6,7,8,9,10]))
