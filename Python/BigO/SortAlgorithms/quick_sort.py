def qsort(lst, start, stop):
    print(f"lst: {lst}")
    print(f"start: {start}")
    print(f"stop: {stop}")

    if start < stop:
        pivot = lst[start]
        low = start
        high = stop

        while low <= high:

            while lst[low] < pivot:
                print(f" Comparing {lst[low]} and {pivot}")
                low += 1
                print(f" low value: {low}")

            while lst[high] > pivot:
                print(f" Comparing {lst[high]} and {pivot} ")
                high -= 1
                print(f" high value : {high}")

            if low <= high:
                print(f" Swapping: {lst[low]}, {lst[high]}")
                lst[low], lst[high] = lst[high], lst[low]
                low += 1
                high -= 1
        print(f" Calling recursively start and high {lst}, {start} ,{high} ")
        qsort(lst, start, high)
        print(f" Calling recursively low and stop {lst}, {low} ,{stop} ")
        qsort(lst, low, stop)


arr = [23, 21, 51, 43, 89, 92, 67]
qsort(arr, 0, len(arr)-1)
print(arr)
