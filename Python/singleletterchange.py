def single_insert_or_delete(s1,s2):
    """
    :param s1: word1
    :param s2: word2
    :return: 0,1,2
    This function is to compare 2 strings and return 0 if they are equal
    return 1 is the words can be made same by single letter addition/deletion. No replacements. Example sin,sink,
    joker,joke,spoke,poke, 2 otherwise
    """

    l1 = [i for i in s1] # convert the string into an array
    l2 = [j for j in s2] # convert the second string in an array

    print l1
    print l2

    l3 = l1 + l2
    l3.sort()
    i = 0
    flag = 0
    #print l3


    if s1.lower() == s2.lower():
        print flag
    elif abs(len(s1)-len(s2)) == 1:
        while i <= (len(l3)-1):
            try:
                if i == len(l3) - 1:
                    flag+=1
                    break
                #print l3[i],l3[i+1]
                if l3[i] == l3[i+1]:
                    pass
                else:
                    #print "Inside else"
                    flag+=1
                    i+=1
            except IndexError as e:
                flag+=1
                pass
            i+=2

        if flag == 0:
            flag = 1
        elif flag > 2:
            flag = 2

    else:
        flag = 2

    return flag

print single_insert_or_delete("Java","Python")
print single_insert_or_delete("dog","god")
print single_insert_or_delete("spoke","poke")
print single_insert_or_delete("programming","programing")
print single_insert_or_delete("this","the")



