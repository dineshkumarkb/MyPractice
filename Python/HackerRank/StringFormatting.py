def print_formatted(number):

    myspace = len(bin(number).lstrip("0b"))
    for i in range(1,number+1):
        print "{} {} {} {}".format(str(i).rjust(myspace),str(oct(i)).lstrip("0").rjust(myspace),str(hex(i)).upper().lstrip("0X").rjust(myspace),
                                   str(bin(i)).lstrip("0b").rjust(myspace))




if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)