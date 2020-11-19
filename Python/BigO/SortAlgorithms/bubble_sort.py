def bubble_sort(lst):
    """
    This sorts a given array using bubble sort algorithm. The time complexity of this algorithm is
    O(n^2).
    :param lst:
    :return:
    """

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


print(bubble_sort([23,11,43,32,55,67,43]))