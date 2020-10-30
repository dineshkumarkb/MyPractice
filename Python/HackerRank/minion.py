def minion_game(string):

    vowels = ['A','E','I','O','U']
    kev = 0
    stu = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kev+=len(string)-i
        else:
            stu+=len(string)-i

    if kev > stu:
        print "Kevin {}".format(kev)
    elif stu > kev:
        print "Stuart {}".format(stu)
    else:
        print "Draw"

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)