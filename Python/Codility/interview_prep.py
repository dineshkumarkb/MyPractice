def fibonacci(n):

    """

    :param n: fibonacci range
    :return:
    """

    if n == 1:
        return 1
    
    a = 0
    b = 1
    count = 0
    while count < n:
        c = a + b
        a, b = b, c
        print(c)
        count += 1
        

#fibonacci(10)

def fib_recursive(n):
    # base case
    if n < 1:
        return 0
    elif n == 1:
        return 1
    
    return fib_recursive(n-1) + fib_recursive(n-2)


#print(fib_recursive(10))


def fib_gen(n):

    a = 0
    b = 1
    count = 0
    while count < n:
        c = a + b
        a,b = b, c
        yield c
        count += 1


myfib = fib_gen(10)
#print(next(myfib))
#print(next(myfib))


def fib_pythonic(n):

    fib_list = [0, 1]
    for i in range(n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    print(fib_list)


#fib_pythonic(10)


def string_check(s):

    if len(s) <= 1:
        return True

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False

    return True


# print(string_check("aac"))


def string_check_with_storage(s):

    if len(s) <= 1:
        return True

    char_dict = dict()

    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    for k,v in char_dict.items():
        if v > 1:
            return False

    return True


#print(string_check("abcdefghijkl"))


def URLify(s):

    char_list = list()
    
    stripped_str = s.rstrip()
    
    for i in stripped_str:
        if i == " ":
            char_list.append("%20")
        else:
            char_list.append(i)
            
    print("".join(char_list))
            

URLify("Mr John Smith   ")