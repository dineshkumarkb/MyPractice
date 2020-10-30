# Merge 2 dicts using the dict.update() method

dict1 = {"a":1,"b":2}
dict2 = {"b":3,"c":4}

dict3 = {}
dict3.update(dict1)
dict3.update(dict2)

print(" The dict3 values are ", dict3)


# Merge 2 dicts using the ** unpacking operator

xs = {"a":1,"b":2}
ys = {"b":3,"c":4}

zs = dict(xs, **ys)

print(" The zs values are ", zs)


# Merge multiple dicts using ** unpacking operator above python 3.6

aa = {"a":1,"b":2}
bb = {"b":3,"c":4}
cc = {"d":5, "e":6}

zz = {**aa,**bb, **cc}

print(" The value of zz is ", zz)


