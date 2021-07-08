s = "eidbaooo"


def sliding_window(elements, window_size):

    if len(elements) <= window_size:
        return elements

    for i in range(len(elements) - window_size + 1):
        print(elements[i:i+window_size])


sliding_window(s, 2)
# print(next(sw_gen))
# print(next(sw_gen))


