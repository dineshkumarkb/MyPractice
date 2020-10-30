def switch_func(func,x,y):
    calc_dict = {
        "add": x + y,
        "sub": x-y,
        "mul": x*y,
        "div": x/y
    }

    return calc_dict.get(func,None)



print(switch_func("add",1,2))
print(switch_func("mul",1,2))
print(switch_func("mod",1,2))