"""
This below program is to illustrate that functions are objects in python
and they are executed even before they are called.
For instance "def" is executed even before the function is called. So any
default arguments will be initialized only once and not every time the function is called.
This is done mainly for performance optimization and will be useful in case of
caching and memoization.
"""

def testDefaultParams(l=[0,1], count = None):
    if count is None:
        return None
    for i in xrange(count):
        l.append(l[-2] + l[-1])
    return l

print testDefaultParams(count = 10)

print testDefaultParams.func_defaults

print testDefaultParams(count=1)


def count_instances(count = 0):

    count+=1

    return count
print count_instances.func_defaults
print count_instances()
print count_instances.func_defaults
print count_instances()






