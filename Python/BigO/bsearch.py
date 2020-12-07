def b_search(lst, n):

    if len(lst) > 1:
        pivot = len(lst)//2
    elif len(lst) == 1:
        pivot = lst[0]
        return 

    if n < lst[pivot]:
        lst = lst[:pivot]
        return b_search(lst, n)
    elif n > lst[pivot]:
        lst = lst[pivot:]
        return b_search(lst, n)
    elif n == lst[pivot]:
        return f" Element found "


print(b_search([2,3,4,5,6,7,8,9,10], 1))
