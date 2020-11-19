def check_perm(s1, s2):
    """
    This function is used to check the permutation of 2 strings
    :param s:
    :return:
    """
    if len(s1) != len(s2):
        return False

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    if s1_sorted == s2_sorted:
        return True

    return False


print(check_perm("god   ", "dog"))