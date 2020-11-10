"""
This program checks if the chars in a string is unique
and returns a boolean value accordingly
"""


def duplicate_checker(input_string):
    """
    The time complexity of this algorithm is O(n)
    :param input_string:
    :return:
    """

    if len(input_string) > 256:
        return False

    char_count = dict()

    for i in input_string:
        print(f" The char count is : {char_count}")
        # Time complexity of in  operator in dict is O(1) because of contains
        if i in char_count:
            char_count[i] += 1
            return False
        else:
            char_count[i] = 1

    return True


#print(duplicate_checker("mystring"))


"""
Below is another string uniqueness checker using bruteforce 
without using additional datastructure
"""

def string_checker(s):
    """
    The time complexity of this algorithm is O(n^2)
    :param s:
    :return:
    """

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


print(string_checker("ddinesh"))