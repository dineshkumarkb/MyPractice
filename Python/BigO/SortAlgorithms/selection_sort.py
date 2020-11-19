def selection_sort(lst):
    """
    The time complexity of this algorithm is O(n^2). This algorithm traverses the array linearly by
    having a minimum value assigned initially. Then on every iteration the minimum value is compared with the
    adjacent value and swapped to the left side of the array.
    Its the opposite of bubble sort. In bubble sort after every pass, the biggest element would reach the rightmost
    here the smallest element will reach the left most.
    :param lst:
    :return:
    """
    for i in range(len(lst)):
        min_idx = i
        print(f"i value: {i}")
        for j in range(i+1, len(lst)):
            print(f"j value: {j}")
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst


print(selection_sort([23,21,43,15,19,32,50]))


