new = [[('name', 'n1')], [('value', 'v1')], [('name', 'n2')], [('value', 'v2')], [('name', 'n3')], [('value', 'v3')]]

print(new[::2])
print(new[1::2])
for x,y in zip(new[::2],new[1::2]):
    print(x[0][1],y[0][1])