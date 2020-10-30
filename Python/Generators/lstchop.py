def chunks(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

output = chunks(list(range(50)),10)
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))