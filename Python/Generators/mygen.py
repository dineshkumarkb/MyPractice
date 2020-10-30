def square_list(mylist):
    for i in mylist:
        yield i*i


output = square_list([1,2,3,4,5,6,7,8,9])

lst = []
for i in output:
    lst.append(i-1)

print(lst)