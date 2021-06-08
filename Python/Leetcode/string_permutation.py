"""

Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

def check_permutation(s1, s2):

    if not s1 or not s2:
        return False

    window_size = len(s1)

    for i in range(len(s2)):
        window = s2[i:i+window_size]
        if is_match(s1, window):
            return True

    return False


def is_match(s1, window):

    if len(s1) != len(window):
        return False

    if s1 == window:
        return True

    from collections import Counter

    s1_count = Counter(s1)
    window_count = Counter(window)

    print(s1_count, window_count)

    if s1_count == window_count:
        return True

    return False


print(check_permutation("ab","eidbaooo"))
