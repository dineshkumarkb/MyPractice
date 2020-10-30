def bingap(n):

    bin_num = str(bin(n))[2:]
    print(f" The binary number is {bin_num} ")
    bin_gap = False
    bin_counter = 0
    bin_max = 0
    for n in bin_num:
        print(n)
        if n == "1":
            print(f" The bin max : {bin_max}")
            print(f" The bin counter : {bin_counter}")
            if bin_max < bin_counter:
                bin_max = bin_counter
            bin_gap = True
            bin_counter = 0
        elif bin_gap:
            bin_counter += 1
    print(f" The binmax value is {bin_max}")


bingap(10)