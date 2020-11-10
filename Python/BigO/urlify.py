"""
This program replaces space with %20 in a string
"""


def urlify(s):
    """
    The time complexity of this algorithm is O(n^2) due to the concatenation.
    += usually makes a copy of the string and copies every character while concatenating.
    So it's 1x + 2x + 3x + ...... + nx ==> O (n^2)
    :param s:
    :return:
    """
    s1 = ""
    for i in s:
        if i == " ":
            s1 += "%20"
        else:
            s1 += i

    return s1


#print(urlify("hi how are you this        is a test "))


def urlify(s):

    """
    The time complexity of this algorithm O(n) because of using join.
    :param s:
    :return:
    """

    output_str = list()

    for i in s:
        if i == " ":
            output_str.append("%20")
        else:
            output_str.append(i)

    print("".join(output_str))


urlify("hi how are you this        is a test ")

