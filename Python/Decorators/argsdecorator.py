def upper(func):
    def inner(*args,**kwargs):
        print(f" Decorating function {func} with args {args} and {kwargs}")
        for ele in args:
            modified_args = []
            modified_args.append(ele.upper())
        return func(*modified_args,**kwargs)
    return inner




@upper
def greet(mystring):
    return mystring


print(greet("Dinesh","Kumar"))