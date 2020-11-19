def merge_sort(lst):

    print(f"lst: {lst}")

    if len(lst) > 1:

        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            print(f"Left: {left}")
            print(f"Right: {right}")

            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst


print(merge_sort([12,10,4,3,2,5,6,8,23]))