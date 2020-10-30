def call_me():
    print(" Inside call me")
    return "Callme"


def function_1():
    test_value = "test123"
    print(" The test value is ", test_value)
    response_value = func_2()
    return test_value


def func_2():
    return 'call from func 2'