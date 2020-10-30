def num_return():
   try:
    x=100
    print("Inside try")
    return x
   finally:
    print("Inside finally")
    x=90
    #return x

print(num_return())
#print(x)

