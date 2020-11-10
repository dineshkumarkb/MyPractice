def compress(s):
    """
    The time complexity of this algorithm is O(n)

    :param s:
    :return:
    """
    char_count = dict()
    encoded_str = list()
    # Time complexity O(n)
    for i in s:
        # Time complexity is O(1)
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    # Time complexity is O(n)
    for i,j in char_count.items():
        encoded_str.append(str(i))
        encoded_str.append(str(j))
    # Time complexity is again O(n)
    return "".join(encoded_str)



print(compress("aaabbc"))