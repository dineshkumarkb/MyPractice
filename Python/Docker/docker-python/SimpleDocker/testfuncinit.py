"""
This is just a test function to prove the initialization of a function
in python test test test test test test test
tesy
"""


def test_params(element, my_list=[]):

    """
    :param element: Element to be appended
    :param my_list:  A list object
    :return: None
    """

    my_list.append(element)

    return my_list


print(test_params(1))
print(test_params(2))
print(test_params(3))
