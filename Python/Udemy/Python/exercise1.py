s ="django"

print (s[0])
print (s[-1])
print (s[:4])
print (s[1:4])
print(s[4:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)


d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print (d1['simple_key'])
print (d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])


age = 4
name = "Sammy"

print("Hello my dog's name is {} and he is {} years old".format(name,age))