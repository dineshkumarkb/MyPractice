"""
This program is to validate the if the string is one edit away
pale pales --> True
pake pale --> True

"""


def check_one_away(s1, s2):
    """
    The time complexity for this function is O(2*s2)
    :param s1:
    :param s2:
    :return:
    """

    str1_length = len(s1)
    str2_length = len(s2)

    string_length_difference = str1_length - str2_length
    if abs(string_length_difference) >= 2:
        return False

    count = 0

    for a,b in zip(s1,s2):
        if a != b:
            count += 1

    if count >= 2:
        return False

    return True



print(check_one_away("pale", "paless"))

